from django.contrib import admin

from ChoseMenu.models import ChoseMenu


# Register your models here.
class ChoseMenuAdmin(admin.ModelAdmin):
    list_display = ['d_id', 's_id','score']


admin.site.register(ChoseMenu, ChoseMenuAdmin)