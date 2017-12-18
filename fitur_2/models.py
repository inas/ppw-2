from django.db import models

# Create your models here.
class Company(models.Model):
    
    id = models.CharField(max_length=400, primary_key=True, default='not-set')
    name = models.CharField(max_length=400, null=True, default='not-set')
    desc = models.CharField(max_length=500, default='not-set', null=True)
    companyType = models.CharField(max_length=100, default='not-set', null=True)
    website = models.URLField(null=True)
    specialities = models.CharField(max_length=100, default='not-set', null=True)
    address = models.CharField(max_length=100, default='not-set', null=True)