from django.urls import path

from Exercise.views import *

urlpatterns = [
    path('menu/', showExerciseMenu),
    path('searchByCalorie/', searchByCalorie),
    path('searchByCircle/', searchByCircle),
    path('searchByDifficulty/', searchByDifficulty)
]
