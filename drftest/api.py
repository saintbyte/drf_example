from rest_framework import routers
from app import api_views  as app_views 
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'application', app_views.ApplicationViewSet)
router.register(r'test', app_views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),   
]