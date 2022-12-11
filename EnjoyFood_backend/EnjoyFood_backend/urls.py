"""EnjoyFood_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.static import serve

import User
from EnjoyFood_backend import settings
from User.views import *
from Dish.views import *
from Chose.views import *

urlpatterns = [

    path('Hello/', Hello),

    path('user/', include('User.urls')),

    path('dish/', include('Dish.urls')),

    path('select/', include('Chose.urls')),

    # path('user/choose/', choose),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT})
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
