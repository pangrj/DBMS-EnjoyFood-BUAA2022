from django.contrib import admin

from Exercise.models import Exercise
from LifeCircle.models import LifeCircle


# Register your models here.
class LifeCircleAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'c_location', 'c_description']


admin.site.register(LifeCircle, LifeCircleAdmin)
