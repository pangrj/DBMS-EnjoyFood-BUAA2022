from django.db import models

from Restaurant.models import Restaurant


# Create your models here.
class Dish(models.Model):
    d_id = models.IntegerField(primary_key=True, null=False)
    d_name = models.CharField(max_length=20, null=False)
    d_category = models.CharField(max_length=20, null=True)
    d_cuisine = models.CharField(max_length=30, null=True)
    d_calories = models.IntegerField(null=False)
    d_price = models.IntegerField(null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
