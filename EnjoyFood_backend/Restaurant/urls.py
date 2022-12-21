from django.urls import path

from Restaurant.views import *

urlpatterns = [
    path('getInfo/', get_restaurant_info)
]
