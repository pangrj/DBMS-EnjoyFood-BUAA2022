from django.contrib import admin

from User.models import *


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_id', 's_name', 's_dorm', 's_gender']


admin.site.register(User, StudentAdmin)