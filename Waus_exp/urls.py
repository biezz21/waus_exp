"""Waus_exp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from APIapp import views
from APIapp.views import DownExpViewset, UpExpViewset, AnnotationViewset

router = routers.DefaultRouter()
router.register('Down_exp', DownExpViewset, basename='Down_exp')
router.register('Up_exp', UpExpViewset, basename='Up_exp')
router.register('Annotations', AnnotationViewset, basename='Annotations')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

