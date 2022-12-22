from django.urls import path

from ExerArea.views import get_exer_area_info

urlpatterns = [
    path('getInfo/', get_exer_area_info)
]
