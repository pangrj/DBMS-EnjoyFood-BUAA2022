from django.contrib import admin

from User.models import *


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['u_id', 'u_name']


admin.site.register(User, StudentAdmin)