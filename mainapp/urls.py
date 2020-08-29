from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from proj02 import settings
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.ProjectSet)
urlpatterns = [
    path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.similarProj),

]