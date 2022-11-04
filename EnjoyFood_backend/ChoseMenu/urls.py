from django.urls import path

from ChoseMenu.views import *

urlpatterns = [
    path("choose/", choose),
    path("delete/", delete_dish),
    path("show/", show_select_dishes)
]
