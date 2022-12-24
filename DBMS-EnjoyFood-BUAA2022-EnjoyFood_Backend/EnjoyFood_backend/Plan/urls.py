from django.urls import path

from Plan.views import *

urlpatterns = [
    path('getInfor/', get_plan_details),
    path('addPlan/', add_plan),
    path('delete/', delete_plan)
]
