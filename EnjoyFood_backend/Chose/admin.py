from django.contrib import admin

from Chose.models import Chose


# Register your models here.
class ChoseMenuAdmin(admin.ModelAdmin):
    list_display = ['d_id', 's_id','score']


admin.site.register(Chose, ChoseMenuAdmin)