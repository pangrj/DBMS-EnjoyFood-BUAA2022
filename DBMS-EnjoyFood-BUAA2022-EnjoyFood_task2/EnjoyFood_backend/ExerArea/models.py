from django.db import models

from LifeCircle.models import LifeCircle


# Create your models here.
class ExerArea(models.Model):
    l_location = models.CharField(max_length=20, null=False)
    l_time = models.CharField(max_length=20, null=False)
    l_info = models.CharField(max_length=20, null=False)
    lifeCircle = models.ForeignKey(LifeCircle, on_delete=models.CASCADE, null=True)

    def get_l_id(self):
        return self.id
