from django.contrib import admin

from student.models import *


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_id', 's_name', 's_dorm', 's_gender']


admin.site.register(Student, StudentAdmin)