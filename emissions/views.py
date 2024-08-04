from rest_framework import viewsets
from .models import Source, Modification, Strategy, Report
from .serializers import SourceSerializer, ModificationSerializer, StrategySerializer, ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class ModificationViewSet(viewsets.ModelViewSet):
    queryset = Modification.objects.all()
    serializer_class = ModificationSerializer

class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
