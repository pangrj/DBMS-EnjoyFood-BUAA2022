from django.contrib import admin

from ExerArea.models import ExerArea


# Register your models here.
class ExerAreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'l_location', 'l_time', 'l_info', 'lifeCircle', 'lifeCircle_id']


admin.site.register(ExerArea, ExerAreaAdmin)
