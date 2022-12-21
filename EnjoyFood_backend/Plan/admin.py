from django.contrib import admin

from Exercise.models import Exercise
from Plan.models import *


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'p_description', 'p_time', 'user', 'calories_in', 'calories_consume']


class PlanOfDishAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'dish']


class PlanOfExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'exercise']


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanOfDish, PlanOfDishAdmin)
admin.site.register(PlanOfExercise, PlanOfExerciseAdmin)
