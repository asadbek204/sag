from django.urls import path
from .views import NewsViewSet

urlpatterns = [
    path('get_news/', NewsViewSet.as_view({'get': 'get_news'}), name='get_news_for_news'),
    path('get_news_by_id/<int:pk>/', NewsViewSet.as_view({'get': 'get_news_by_id'}), name='get_news_by_id'),
]