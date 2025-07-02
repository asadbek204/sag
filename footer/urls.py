from django.urls import path
from .views import FooterViewSet

urlpatterns = [
    path('get_phone_number/', FooterViewSet.as_view({'get': 'get_phone_number'}), name='get_phone_number'),
    path('get_social_media/', FooterViewSet.as_view({'get': 'get_social_media'}), name='get_social_media'),
]