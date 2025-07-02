from django.urls import path
from .views import MethodViewSet

urlpatterns = [
    path('get_contents/', MethodViewSet.as_view({'get': 'get_contents'}), name='get_contents'),
    path('get_materials/', MethodViewSet.as_view({'get': 'get_materials'}), name='get_materials'),
    path('get_product_gallery/', MethodViewSet.as_view({'get': 'get_product_gallery'}), name='get_product_gallery'),
    path('get_about_method/', MethodViewSet.as_view({'get': 'get_about_method'}), name='get_about_method'),
]
