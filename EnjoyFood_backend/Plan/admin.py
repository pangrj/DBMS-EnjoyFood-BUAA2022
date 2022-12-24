from django.contrib import admin

from Exercise.models import Exercise
from Plan.models import *


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'p_description', 'p_time', 'user', 'calories_in', 'calories_consume']


class PlanOfDishAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'plan_id', 'dish', 'dish_id']


class PlanOfExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'plan_id', 'exercise', 'exercise_id']


# class CircleOfPlanAdmin(admin.ModelAdmin):
#     list_display = ['id', 'plan', 'plan_id', 'circle', 'circle_id']


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanOfDish, PlanOfDishAdmin)
admin.site.register(PlanOfExercise, PlanOfExerciseAdmin)
# admin.site.register(CircleOfPlan, CircleOfPlanAdmin)
