from django.db import models
from datetime import date

class AnnualReport(models.Model):
    """
    AnnualReport aggregates all emissions for a year.
    """
    title = models.CharField(max_length=200, blank=True, null=True)
    report_date = models.DateField()

class EmissionSource(models.Model):
    """
    EmissionSource represents a source that generates GHG emissions.
    """
    annual_report = models.ForeignKey(AnnualReport, on_delete=models.CASCADE, blank=True, null=True)
    detail = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    factor = models.FloatField(blank=True, null=True)
    total_ghg = models.FloatField(blank=True, null=True, help_text="Unit in kg")
    duration = models.PositiveIntegerField(blank=True, null=True)
    year_acquired = models.PositiveSmallIntegerField(blank=True, null=True)

    def compute_yearly_emission(self, current_year):
        if self.duration and self.year_acquired:
            operational_years = current_year - self.year_acquired
            if operational_years >= self.duration:
                return 0
            return self.total_ghg / self.duration
        return self.total_ghg

class EmissionAdjustment(models.Model):
    emission_source = models.ForeignKey(EmissionSource, on_delete=models.CASCADE)
    adjustment_type = models.CharField(max_length=20, choices=[('ratio', 'Ratio'), ('factor', 'Factor')])
    adjustment_value = models.FloatField()
    adjustment_date = models.DateField()

    def apply_adjustment(self):
        if self.adjustment_type == 'ratio':
            return self.emission_source.amount * self.adjustment_value
        elif self.adjustment_type == 'factor':
            return self.adjustment_value
        return self.emission_source.amount

class EmissionStrategy(models.Model):
    annual_report = models.ForeignKey(AnnualReport, on_delete=models.CASCADE)
    strategy_name = models.CharField(max_length=200)
    adjustments = models.ManyToManyField(EmissionAdjustment)

    def compute_total_emission(self, current_year):
        total_emission = 0
        for adjustment in self.adjustments.all():
            adjusted_value = adjustment.apply_adjustment()
            source = adjustment.emission_source
            yearly_emission = source.compute_yearly_emission(current_year)
            total_emission += adjusted_value * yearly_emission
        return total_emission
