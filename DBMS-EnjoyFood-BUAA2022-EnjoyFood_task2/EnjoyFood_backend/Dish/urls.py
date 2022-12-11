from django.urls import path

from Dish.views import *

urlpatterns = [
    path('menu/', showNotSelectMenu),
    path('initial/', initial),
    path('searchByName/', searchByName)
]
