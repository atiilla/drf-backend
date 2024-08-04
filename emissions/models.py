from django.db import models
from datetime import date

class Report(models.Model):
    """
    The Report is the sum of all the emissions. It should be done once a year
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()

class Source(models.Model):
    """
    An Emission is every source that generates GreenHouse gases (GHG).
    It could be defined as source x emission_factor = total
    """
    report = models.ForeignKey(Report, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    emission_factor = models.FloatField(blank=True, null=True)
    total_emission = models.FloatField(blank=True, null=True, help_text="Unit in kg")
    lifetime = models.PositiveIntegerField(blank=True, null=True)
    acquisition_year = models.PositiveSmallIntegerField(blank=True, null=True)

    def calculate_emission_for_year(self, year):
        if self.lifetime:
            years_in_use = year - self.acquisition_year
            if years_in_use > self.lifetime:
                return 0
            return self.total_emission / self.lifetime
        return self.total_emission

class Modification(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    modification_type = models.CharField(max_length=20, choices=[('ratio', 'Ratio'), ('emission_factor', 'Emission Factor')])
    modification_value = models.FloatField()
    date = models.DateField()

    def apply_modification(self):
        if self.modification_type == 'ratio':
            return self.source.value * self.modification_value
        elif self.modification_type == 'emission_factor':
            return self.modification_value
        return self.source.value

class Strategy(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    modifications = models.ManyToManyField(Modification)

    def calculate_total_emission_for_year(self, year):
        total_emission = 0
        for modification in self.modifications.all():
            modified_value = modification.apply_modification()
            total_emission += modified_value * self.source.emission_factor
        return total_emission
