from django.db import models

from Dish.models import Dish
from Exercise.models import Exercise
from LifeCircle.models import LifeCircle
from User.models import User


# Create your models here.
class Plan(models.Model):
    p_name = models.CharField(max_length=20, null=False)
    p_description = models.CharField(max_length=20, null=False)
    p_time = models.DateTimeField(null=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    calories_in = models.IntegerField(null=True)
    calories_consume = models.IntegerField(null=True)

    def get_p_id(self):
        return self.id


# class CircleOfPlan(models.Model):
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
#     circle = models.ForeignKey(LifeCircle, on_delete=models.CASCADE, null=False)


class PlanOfDish(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=False)

    def get_p_d_id(self):
        return self.id


class PlanOfExercise(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)

    def get_p_e_id(self):
        return self.id
