from django.db import models

from LifeCircle.models import LifeCircle


# Create your models here.
class Restaurant(models.Model):
    re_name = models.CharField(max_length=20, null=False)
    re_category = models.CharField(max_length=20, null=False)
    re_description = models.CharField(max_length=50, null=False)
    lifeCircle = models.ForeignKey(LifeCircle, on_delete=models.CASCADE, null=True)
