import random
from datetime import datetime
from django.core.management.base import BaseCommand
from emissions.models import Source, Report, Modification, Strategy

class Command(BaseCommand):
    help = 'Generate dummy data'

    def handle(self, *args, **kwargs):
        report = Report.objects.create(name='Dummy Report', date=datetime.now())
        
        for i in range(10):
            source = Source.objects.create(
                report=report,
                description=f'Source {i}',
                value=random.uniform(10, 100),
                emission_factor=random.uniform(1, 10),
                total_emission=random.uniform(100, 1000),
                lifetime=random.randint(1, 10),
                acquisition_year=random.randint(2010, 2020)
            )
            mod_type = random.choice(['ratio', 'emission_factor'])
            mod_value = random.uniform(0.5, 2) if mod_type == 'ratio' else random.uniform(1, 10)
            Modification.objects.create(
                source=source,
                modification_type=mod_type,
                modification_value=mod_value,
                date=datetime.now()
            )

        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully'))
