from django.urls import path
from .views import RoomsViewSet

urlpatterns = [
    path('get_rooms/', RoomsViewSet.as_view({'get': 'get_rooms'}), name='get_rooms'),
    path('get_rooms_images_by_room_id/<int:pk>/', RoomsViewSet.as_view({'get': 'get_rooms_images_by_room_id'}),
         name='get_rooms_images_by_room_id'),
]
