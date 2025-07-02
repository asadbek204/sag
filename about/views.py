from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import (
    AboutCompany,
    BriefAbout,
    ProductionVolume,
    Gallery,
    AboutProduction
)
from .serializers import (
    GetAboutCompanySerializer,
    GetBriefAboutSerializer,
    GetProductionVolumeSerializer,
    GetGallerySerializer,
    GetAboutProductionSerializer
)
from drf_yasg.utils import swagger_auto_schema


class AboutViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get About Company",
        operation_summary="Get About Company",
        responses={
            200: GetAboutCompanySerializer(),
        },
        tags=['about']
    )
    def get_about_company(self, request, *args, **kwargs):
        about_company = AboutCompany.objects.all().first()
        serializer = GetAboutCompanySerializer(about_company, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Brief About",
        operation_summary="Get Brief About",
        responses={
            200: GetBriefAboutSerializer(),
        },
        tags=['about']
    )
    def get_brief_about(self, request, *args, **kwargs):
        brief_about = BriefAbout.objects.all().first()
        serializer = GetBriefAboutSerializer(brief_about, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Production Volume",
        operation_summary="Get Production Volume",
        responses={
            200: GetProductionVolumeSerializer(),
        },
        tags=['about']
    )
    def get_production_volume(self, request, *args, **kwargs):
        production_volume = ProductionVolume.objects.all()
        serializer = GetProductionVolumeSerializer(production_volume, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get About Production",
        operation_summary="Get About Production",
        responses={
            200: GetAboutProductionSerializer(),
        },
        tags=['about']
    )
    def get_about_production(self, request, *args, **kwargs):
        about_production = AboutProduction.objects.all().first()
        serializer = GetAboutProductionSerializer(about_production, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Gallery",
        operation_summary="Get Gallery",
        responses={
            200: GetGallerySerializer(),
        },
        tags=['about']
    )
    def get_gallery(self, request, *args, **kwargs):
        gallery = Gallery.objects.all()
        serializer = GetGallerySerializer(gallery, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
