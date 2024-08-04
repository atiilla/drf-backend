from rest_framework import viewsets
from .models import EmissionSource, EmissionAdjustment, EmissionStrategy, AnnualReport
from .serializers import EmissionSourceSerializer, EmissionAdjustmentSerializer, EmissionStrategySerializer, AnnualReportSerializer

class AnnualReportViewSet(viewsets.ModelViewSet):
    queryset = AnnualReport.objects.all()
    serializer_class = AnnualReportSerializer

class EmissionSourceViewSet(viewsets.ModelViewSet):
    queryset = EmissionSource.objects.all()
    serializer_class = EmissionSourceSerializer

class EmissionAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = EmissionAdjustment.objects.all()
    serializer_class = EmissionAdjustmentSerializer

class EmissionStrategyViewSet(viewsets.ModelViewSet):
    queryset = EmissionStrategy.objects.all()
    serializer_class = EmissionStrategySerializer
