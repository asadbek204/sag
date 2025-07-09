from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Room, RoomImage
from .serializers import RoomsSerializer, GetRoomsSerializer
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema


class RoomsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Rooms",
        operation_summary="Get Rooms",
        responses={
            200: RoomsSerializer(),
        },
        tags=['rooms']
    )
    def get_rooms(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomsSerializer(rooms, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Room Images",
        operation_summary="Get Room Images",
        responses={
            200: GetRoomsSerializer(),
        },
        tags=['rooms']
    )
    def get_rooms_images_by_room_id(self, request, *args, **kwargs):
        room = Room.objects.filter(id=kwargs['pk']).first()
        if room is None:
            return Response(data={'error': _('Room not found')}, status=status.HTTP_404_NOT_FOUND)
        room_images = RoomImage.objects.filter(room=room)
        serializer = GetRoomsSerializer(room_images, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
