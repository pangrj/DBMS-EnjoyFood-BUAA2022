from django.urls import path

from Plan.views import *
from User.views import *

urlpatterns = [

    path('login/', login),
    path('register/', register),

    path('modify/', modify_infor),
    path('changePassword/', change_password),
    path('getAvatar/', get_avatar),

    path('getInfor/', get_infor),

    path('getPlanCal/', get_latest_plan_calories),

    path('getPlans/', get_plan_by_u_name),

    path('load/', upLoadImg)
]
