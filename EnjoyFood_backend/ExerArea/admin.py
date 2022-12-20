from django.contrib import admin

from ExerArea.models import ExerArea


# Register your models here.
class ExerAreaAdmin(admin.ModelAdmin):
    list_display = ['l_location', 'l_time', 'l_info', 'lifeCircle']


admin.site.register(ExerArea, ExerAreaAdmin)
