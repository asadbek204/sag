from .models import CallCenter, SocialMedia
from rest_framework.viewsets import ViewSet
from .seriializers import CallCenterSerializer, SocialMediaSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class FooterViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Phone Number",
        operation_summary="Get Phone Number",
        responses={
            200: CallCenterSerializer(),
        },
        tags=['footer']
    )
    def get_phone_number(self, request, *args, **kwargs):
        phone_numbers = CallCenter.objects.all()
        serializer = CallCenterSerializer(phone_numbers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Social Media",
        operation_summary="Get Social Media",
        responses={
            200: SocialMediaSerializer(),
        },
        tags=['footer']
    )
    def get_social_media(self, request, *args, **kwargs):
        social_medias = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(social_medias, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
