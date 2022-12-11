from django.contrib import admin

from Dish.models import *


# Register your models here.
class DishAdmin(admin.ModelAdmin):
    list_display = ['d_id', 'd_name', 'd_category', 'd_cuisine', 'd_calories', 'd_price']


admin.site.register(Dish, DishAdmin)
