import random
from datetime import datetime
from django.core.management.base import BaseCommand
from emissions.models import EmissionSource, AnnualReport, EmissionAdjustment

class Command(BaseCommand):
    help = 'Generate dummy data for testing'

    def handle(self, *args, **kwargs):
        # Create an AnnualReport
        report = AnnualReport.objects.create(title='Dummy Report', report_date=datetime.now())
        
        # Create EmissionSource instances and EmissionAdjustment instances
        for i in range(10):
            source = EmissionSource.objects.create(
                annual_report=report,
                detail=f'Source {i}',
                amount=random.uniform(10, 100),
                factor=random.uniform(1, 10),
                total_ghg=random.uniform(100, 1000),
                duration=random.randint(1, 10),
                year_acquired=random.randint(2010, 2020)
            )
            adj_type = random.choice(['ratio', 'factor'])
            adj_value = random.uniform(0.5, 2) if adj_type == 'ratio' else random.uniform(1, 10)
            EmissionAdjustment.objects.create(
                emission_source=source,
                adjustment_type=adj_type,
                adjustment_value=adj_value,
                adjustment_date=datetime.now()
            )

        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully'))
