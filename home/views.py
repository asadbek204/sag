from rest_framework.viewsets import ViewSet

from catalog.serializers import GetCarpetModelsSerializer
from .serializers import (
    HeaderSerializer,
    CatalogSerializer,
    GetBlogSerializer,
    QuestionSerializer,
    CollectionSerializer,
    CarpetModelSerializer,
    CarpetSerializer
)
from .models import Header, Questions, Collection
from rest_framework.response import Response
from rest_framework import status
from catalog.models import Catalog
from blog.models import Blog
from catalog.models import CarpetModel, Carpet
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Header",
        operation_summary="Get Header",
        responses={
            200: HeaderSerializer(),
        },
        tags=['home']
    )
    def get_header(self, request, *args, **kwargs):
        head = Header.objects.all().first()
        serializer = HeaderSerializer(head, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Catalogs",
        operation_summary="Get Catalogs",
        responses={
            200: CatalogSerializer(),
        },
        tags=['home']
    )
    def get_catalogs(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Collections",
        operation_summary="Get Collections",
        responses={
            200: CollectionSerializer(),
        },
        tags=['home']
    )
    def get_collections(self, request, *args, **kwargs):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Blogs",
        operation_summary="Get Blogs",
        responses={
            200: GetBlogSerializer(),
        },
        tags=['home']
    )
    def get_blogs(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = GetBlogSerializer(blogs, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Questions",
        operation_summary="Get Questions",
        responses={
            200: QuestionSerializer(),
        },
        tags=['home']
    )
    def get_questions(self, request, *args, **kwargs):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get News",
        operation_summary="Get News",
        responses={
            200: CarpetModelSerializer(),
        },
        tags=['home']
    )
    def get_news(self, request, *args, **kwargs):
        new_carpets = Carpet.objects.filter(collection_type=2)
        new_carpet_models = CarpetModel.objects.filter(collection_type=2)

        serialized_carpets = CarpetSerializer(new_carpets, many=True, context={'request': request}).data
        serialized_carpet_models = CarpetModelSerializer(new_carpet_models, many=True,
                                                         context={'request': request}).data

        combined = [
                       {**item} for item in serialized_carpets
                   ] + [
                       {**item} for item in serialized_carpet_models
                   ]

        return Response(data=combined, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Search Carpet",
        operation_summary="Search Carpet",
        manual_parameters=[
            openapi.Parameter(
                'search', openapi.IN_QUERY, description="search carpets by carpets or carpets model",
                type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: GetCarpetModelsSerializer(),
        },
        tags=['home']
    )
    def search_carpets(self, request, *args, **kwargs):
        search = request.GET.get('search', '').strip()
        if not search:
            return Response(data={'error': _('Search query is required')}, status=status.HTTP_400_BAD_REQUEST)
        queryset = CarpetModel.objects.filter(
            Q(name__icontains=search) |
            Q(model__name__icontains=search)
        )
        serializer = GetCarpetModelsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
