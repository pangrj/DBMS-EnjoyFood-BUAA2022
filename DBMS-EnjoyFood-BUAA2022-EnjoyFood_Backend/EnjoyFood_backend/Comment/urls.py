from django.urls import path

from Comment.views import *

urlpatterns = [
    path('publishComment/', publish_comment),
    path('getCommentOfPlan/', get_comment_of_Plan)
]
