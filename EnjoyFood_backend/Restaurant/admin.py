from django.contrib import admin

from Restaurant.models import Restaurant


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['re_name', 're_category', 're_description', 'lifeCircle']


admin.site.register(Restaurant, RestaurantAdmin)
