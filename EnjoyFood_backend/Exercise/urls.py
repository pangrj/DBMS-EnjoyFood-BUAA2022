from django.urls import path

from Exercise.views import *

urlpatterns = [
    path('menu/', showExerciseMenu)
]
