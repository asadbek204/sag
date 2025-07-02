from django.urls import path
from .views import CatalogViewSet

urlpatterns = [
    path('filter_choices/<int:pk>/', CatalogViewSet.as_view({'get': 'filter_choices'}), name='filter_choices'),
    path('filter_choices_for_carpet_model/<int:pk>/',
         CatalogViewSet.as_view({'get': 'filter_choices_for_carpet_model'}), name='filter_choices_for_carpet_model'),
    path('get_catalogs/', CatalogViewSet.as_view({'get': 'get_catalogs'}), name='get_catalogs'),
    # carpet
    path('get_carpets_by_catalog_id/<int:pk>/', CatalogViewSet.as_view({'get': 'get_carpets_by_catalog_id'}),
         name='get_carpets_by_catalog_id'),
    # collection
    path('get_carpet_models_by_carpet_id/<int:pk>/', CatalogViewSet.as_view({'get': 'get_carpet_models_by_carpet_id'}),
         name='get_carpet_models_by_carpet_id'),
    path('filter_and_sort_carpets/<int:pk>/', CatalogViewSet.as_view({'get': 'filter_and_sort_carpets'}),
         name='filter_and_sort_carpets'),
    path('filter_and_sort_carpets_for_carpet_model/<int:pk>/',
         CatalogViewSet.as_view({'get': 'filter_and_sort_carpets_for_carpet_model'}),
         name='filter_and_sort_carpets_for_carpet_model'),
    path('get_carpet_model_by_id/<int:pk>/', CatalogViewSet.as_view({'get': 'get_carpet_model_by_id'}),
         name='get_carpet_model_by_id'),
]
