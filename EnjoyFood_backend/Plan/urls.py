from django.urls import path

from Plan.views import *

urlpatterns = [
    path('getInfor/', get_plan_details)
]
