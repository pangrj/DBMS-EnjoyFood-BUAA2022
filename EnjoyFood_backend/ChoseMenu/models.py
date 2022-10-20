from django.db import models


# Create your models here.
class ChoseMenu(models.Model):
    s_id = models.IntegerField(null=False)
    d_id = models.IntegerField(null=False)
    score = models.IntegerField(null=True)
