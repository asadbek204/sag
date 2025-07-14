from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('get_header/', HomeViewSet.as_view({'get': 'get_header'}), name='get_header'),
    path('get_catalogs/', HomeViewSet.as_view({'get': 'get_catalogs'}), name='get_catalogs'),
    path('get_collections/', HomeViewSet.as_view({'get': 'get_collections'}), name='get_collections'),
    path('get_blogs/', HomeViewSet.as_view({'get': 'get_blogs'}), name='get_blogs'),
    path('get_questions/', HomeViewSet.as_view({'get': 'get_questions'}), name='get_questions'),
    path('get_news/', HomeViewSet.as_view({'get': 'get_news'}), name='get_news'),
    path('search/', HomeViewSet.as_view({'get': 'search_carpets'}), name='search'),
    path('get_filter_and_sort_search_choices/', HomeViewSet.as_view({'get': 'get_filter_and_sort_search_choices'}),
         name='get_filter_and_sort_search_choices'),
    path('filter_and_sort_carpet_model_for_search/',
         HomeViewSet.as_view({'get': 'filter_and_sort_carpet_model_for_search'}),
         name='filter_and_sort_carpet_model_for_search'),
]
