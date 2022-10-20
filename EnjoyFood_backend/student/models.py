from django.db import models


# Create your models here.

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True, null=False)
    s_password = models.CharField(max_length=20, null=False)
    s_name = models.CharField(max_length=20, null=True)
    s_dorm = models.CharField(max_length=30, null=True)
    s_gender = models.CharField(max_length=30, null=True)
