from django.contrib import admin

from Restaurant.models import Restaurant


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 're_name', 're_category', 're_description', 'lifeCircle', 'lifeCircle_id']


admin.site.register(Restaurant, RestaurantAdmin)
