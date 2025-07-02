from django.urls import path
from .views import DiscountViewSet

urlpatterns = [
    path('get_main_discounted_carpets/', DiscountViewSet.as_view({'get': 'get_main_discounted_carpets'}),
         name='get_main_discounted_carpets'),
    path('get_discounted_carpet_models/', DiscountViewSet.as_view({'get': 'get_discounted_carpet_models'}),
         name='get_discounted_carpet_models'),
    path('get_main_discounted_carpet_model/<int:pk>/',
         DiscountViewSet.as_view({'get': 'get_main_discounted_carpet_model'}),
         name='get_main_discounted_carpet_model'),
]
