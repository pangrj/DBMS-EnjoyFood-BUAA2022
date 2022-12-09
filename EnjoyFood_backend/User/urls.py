from django.urls import path

from User.views import *

urlpatterns = [

    path('login/', login),
    path('register/', register),

    path('modify/', modify_infor)
]
