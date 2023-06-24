from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    company_mission = models.CharField(max_length=1000)
    company_vission = models.CharField(max_length=1000)
    company_objective = models.CharField(max_length=1000)