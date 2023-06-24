from rest_framework import serializers
from .models import CompanyInfo

class CompanyInfoSerializer(serializers.ModelSerializer):
    company_mission = serializers.CharField(max_length=1000)
    company_vission = serializers.CharField(max_length=1000)
    company_objective = serializers.CharField(max_length=1000)

    class Meta:
        model = CompanyInfo
        fields = ('__all__')
        