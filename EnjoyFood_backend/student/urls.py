from django.urls import path

from student.views import *

urlpatterns = [
    path('login/', login),
    path('modify/', modify_infor)
]
