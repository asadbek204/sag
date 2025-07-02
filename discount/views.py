from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from catalog.models import CarpetModel, Carpet
from drf_yasg.utils import swagger_auto_schema
from catalog.serializers import (
    DiscountedCarpetSerializer,
    DiscountedCarpetModelSerializer,
)
from django.utils.translation import gettext_lazy as _


class DiscountViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Discounted Carpets For Discount Page",
        operation_summary="Get Discounted Carpets For Discount Page",
        responses={
            200: DiscountedCarpetSerializer(),
        },
        tags=['discount']
    )
    def get_main_discounted_carpets(self, request, *args, **kwargs):
        carpets = Carpet.objects.filter(collection_type=3)
        serializer = DiscountedCarpetSerializer(carpets, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Discounted Carpet Models For Discount Page",
        operation_summary="Get Discounted Carpets Models For Discount Page",
        responses={
            200: DiscountedCarpetModelSerializer(),
        },
        tags=['discount']
    )
    def get_main_discounted_carpet_model(self, request, *args, **kwargs):
        carpet = Carpet.objects.filter(id=kwargs['pk'], collection_type=3).first()
        if carpet is None:
            return Response(data={'error': _('Carpet not found or Carpet is not New')}, status=status.HTTP_404_NOT_FOUND)
        carpet_models = CarpetModel.objects.filter(model=carpet, collection_type=3)
        serializer = DiscountedCarpetModelSerializer(carpet_models, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Discounted Carpet Models B",
        operation_summary="Get Discounted Carpets Models B",
        responses={
            200: DiscountedCarpetModelSerializer(),
        },
        tags=['discount']
    )
    def get_discounted_carpet_models(self, request, *args, **kwargs):
        carpet_models = CarpetModel.objects.filter(collection_type=3)
        serializer = DiscountedCarpetModelSerializer(carpet_models, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

