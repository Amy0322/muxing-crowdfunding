from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from proj02 import settings
from . import views
from rest_framework import routers
from rest_framework_nested import routers
# from views import fundraisingsViewSet, chartViewSet, pointViewSet, rateViewSet

router = routers.DefaultRouter()
router.register('MyAPI', views.UserView)

# domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
# domains_router.register(r'nameservers', fundraisingsViewSet)
urlpatterns = [
    # path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', views.similarProj),
    # path(r'^', include(domains_router.urls)),

]