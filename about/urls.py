from django.urls import path
from .views import AboutViewSet

urlpatterns = [
    path('get_about_company/', AboutViewSet.as_view({'get': 'get_about_company'}), name='get_about_company'),
    path('get_brief_about/', AboutViewSet.as_view({'get': 'get_brief_about'}), name='get_brief_about'),
    path('get_production_volume/', AboutViewSet.as_view({'get': 'get_production_volume'}), name='get_production_volume'),
    path('get_about_production/', AboutViewSet.as_view({'get': 'get_about_production'}), name='get_about_production'),
    path('get_gallery/', AboutViewSet.as_view({'get': 'get_gallery'}), name='get_gallery'),
]