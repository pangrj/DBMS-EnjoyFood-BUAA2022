from django.contrib import admin

from Exercise.models import Exercise


# Register your models here.
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'sp_name', 'sp_content', 'sp_difficulty', 'sp_calories', 'sp_time', 'exerArea']


admin.site.register(Exercise, ExerciseAdmin)
