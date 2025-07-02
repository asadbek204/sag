from django.urls import path
from .views import BlogViewSet

urlpatterns = [
    path('get_all_blogs/', BlogViewSet.as_view({'get': 'get_all'}), name='get_all_blogs'),
    path('get_blog_by_id/<int:pk>/', BlogViewSet.as_view({'get': 'get_by_id'}), name='get_blog_by_id'),
]