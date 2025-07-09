from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import ContactSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ContactViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Contact",
        operation_summary="Contact",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='full_name'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='phone_number'),
                'city': openapi.Schema(type=openapi.TYPE_INTEGER, description='city'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='address'),
                'comment': openapi.Schema(type=openapi.TYPE_STRING, description='comment'),
            },
            required=['full_name', 'phone_number']
        ),
        responses={201: ContactSerializer()},
        tags=['contact'],
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

