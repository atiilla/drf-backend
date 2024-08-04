from rest_framework import serializers
from .models import EmissionSource, EmissionAdjustment, EmissionStrategy, AnnualReport

class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualReport
        fields = '__all__'

class EmissionSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionSource
        fields = '__all__'

class EmissionAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionAdjustment
        fields = '__all__'

class EmissionStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionStrategy
        fields = '__all__'
