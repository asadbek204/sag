from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import (
    Content,
    Material,
    ProductGallery, AboutMethod,
)
from .serializers import (
    GetContentSerializer,
    GetMaterialSerializer,
    GetProductGallerySerializer, AboutMethodSerializer,
)
from drf_yasg.utils import swagger_auto_schema


class MethodViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Contents",
        operation_summary="Get Contents",
        responses={
            200: GetContentSerializer(),
        },
        tags=['method']
    )
    def get_contents(self, request, *args, **kwargs):
        contents = Content.objects.all()
        serializer = GetContentSerializer(contents, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Materials",
        operation_summary="Get Materials",
        responses={
            200: GetMaterialSerializer(),
        },
        tags=['method']
    )
    def get_materials(self, request, *args, **kwargs):
        materials = Material.objects.all()
        serializer = GetMaterialSerializer(materials, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Product Gallery",
        operation_summary="Get Product Gallery",
        responses={
            200: GetProductGallerySerializer(),
        },
        tags=['method']
    )
    def get_product_gallery(self, request, *args, **kwargs):
        product_gallery = ProductGallery.objects.all()
        serializer = GetProductGallerySerializer(product_gallery, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get About Method",
        operation_summary="Get About Method",
        responses={
            200: AboutMethodSerializer(),
        },
        tags=['method']
    )
    def get_about_method(self, request, *args, **kwargs):
        about_method = AboutMethod.objects.all().first()
        serializer = AboutMethodSerializer(about_method, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
