from django.urls import path

from Dish.views import *

urlpatterns = [
    path('menu/', showDishMenu),
    path('initial/', initial),
    path('searchByName/', searchByName),
    path('searchByCategory/', searchByCategory),
    path('searchByCalorie/', searchByCalorie),
    path('searchByCircle/', searchByCircle),
    path('searchByRestaurant/', searchByRestaurant)
]
