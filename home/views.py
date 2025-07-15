from rest_framework.viewsets import ViewSet

from catalog.serializers import (
    GetCarpetModelsSerializer,
    RoomSerializer,
    ColorSerializer,
    ShapeSerializer,
    StyleSerializer,
    GetPriceSerializer
)
from rooms.models import Room
from .serializers import (
    HeaderSerializer,
    CatalogSerializer,
    GetBlogSerializer,
    QuestionSerializer,
    CollectionSerializer,
    CarpetModelSerializer,
    CarpetSerializer,
    GetCollectionSerializer, NewsCarpetCollectionSerializer, NewsCarpetDetailSerializer
)
from .models import Header, Questions, Collection, CarpetCollectionNews, CarpetDetailNews
from rest_framework.response import Response
from rest_framework import status
from catalog.models import Catalog, Style, Color, Shape, Price
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
            200: 'ok',
        },
        tags=['home']
    )
    def get_news(self, request, *args, **kwargs):
        # new_carpets = Carpet.objects.filter(collection_type=2)
        # new_carpet_models = CarpetModel.objects.filter(collection_type=2)
        #
        # serialized_carpets = CarpetSerializer(new_carpets, many=True, context={'request': request}).data
        # serialized_carpet_models = CarpetModelSerializer(new_carpet_models, many=True,
        #                                                  context={'request': request}).data
        #
        # combined = [
        #                {**item} for item in serialized_carpets
        #            ] + [
        #                {**item} for item in serialized_carpet_models
        #            ]
        carpet = CarpetCollectionNews.objects.all()
        carpet_model = CarpetDetailNews.objects.all()

        serializer_collection = NewsCarpetCollectionSerializer(carpet, many=True, context={'request': request}).data
        serializer_model = NewsCarpetDetailSerializer(carpet_model, many=True, context={'request': request}).data

        combined = [
                       {**item} for item in serializer_collection
                   ] + [
                       {**item} for item in serializer_model
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

    @swagger_auto_schema(
        operation_description="Get Filter Choices For Collections in Search",
        operation_summary="Get Filter Choices For Collections in Search",
        responses={
            200: openapi.Response(
                description="Filter data for catalog",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        # simplified, or use ref to FilterSerializer
                        'collections': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'styles': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'rooms': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'colors': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'shapes': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'prices': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                        'labels': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                    },
                    required=['catalog', 'collections', 'rooms', 'colors', 'shapes', 'prices'],  # styles is optional
                )
            ),
            404: 'Catalog not found',
        },
        tags=['home']
    )
    def get_filter_and_sort_search_choices(self, request, *args, **kwargs):
        collections = Carpet.objects.all()
        styles = Style.objects.all()
        rooms = Room.objects.all()
        colors = Color.objects.all()
        shapes = Shape.objects.all()
        prices = Price.objects.all()

        response_data = {
            'collections': GetCollectionSerializer(collections, many=True, context={'request': request}).data,
            'rooms': RoomSerializer(rooms, many=True, context={'request': request}).data,
            'colors': ColorSerializer(colors, many=True, context={'request': request}).data,
            'shapes': ShapeSerializer(shapes, many=True, context={'request': request}).data,
            'styles': StyleSerializer(styles, many=True, context={'request': request}).data,
            'prices': GetPriceSerializer(prices, many=True, context={'request': request}).data,
            'labels': {
                'catalog': _('Catalog'),
                'collections': _('Collections'),
                'rooms': _('Rooms'),
                'colors': _('Colors'),
                'shapes': _('Shapes'),
                'styles': _('Styles'),
                'prices': _('Prices'),
            }
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Filter and Sort For Carpet in Search",
        operation_summary="Filter and Sort For Carpet in Search",
        manual_parameters=[
            openapi.Parameter(
                'query', openapi.IN_QUERY, description='search',
                type=openapi.TYPE_STRING
            ),openapi.Parameter(
                'sort_by', openapi.IN_QUERY, description="1=New, 2=Hit, 3=Sale",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'styles', openapi.IN_QUERY,
                description='Comma-separated list of style IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'collections', openapi.IN_QUERY,
                description='Comma-separated list of collection IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'rooms', openapi.IN_QUERY,
                description='Comma-separated list of room IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'colors', openapi.IN_QUERY,
                description='Comma-separated list of color IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'shapes', openapi.IN_QUERY,
                description='Comma-separated list of shape IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'prizes', openapi.IN_QUERY,
                description='Comma-separated list of prize IDs', type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: GetCarpetModelsSerializer(),
        },
        tags=['home']
    )
    def filter_and_sort_carpet_model_for_search(self, request, *args, **kwargs):
        data = request.GET
        query = data.get('query', '').strip()
        sort_by = data.get('sort_by')

        def get_list(param):
            return [int(x) for x in data.get(param, "").split(",") if x.strip().isdigit()]

        # Extract filters
        collection_ids = get_list("collections")
        style_ids = get_list("styles")
        room_ids = get_list("rooms")
        color_ids = get_list("colors")
        shape_ids = get_list("shapes")
        price_ids = get_list("price")

        is_filter_active = any([collection_ids, style_ids, room_ids, color_ids, shape_ids, price_ids])

        if is_filter_active:
            queryset = CarpetModel.objects.all()
        else:
            queryset = CarpetModel.objects.all()
            if query:
                queryset = queryset.filter(name__icontains=query)

        if sort_by == "1":
            queryset = queryset.filter(collection_type=2)  # New
        elif sort_by == "2":
            queryset = queryset.filter(collection_type=4)  # Hit
        elif sort_by == "3":
            queryset = queryset.filter(collection_type=3)  # Sale

        if style_ids:
            queryset = queryset.filter(style_id__in=style_ids)
        if room_ids:
            queryset = queryset.filter(room_id__in=room_ids)
        if color_ids:
            queryset = queryset.filter(color_id__in=color_ids)
        if shape_ids:
            queryset = queryset.filter(size__shape_id__in=shape_ids).distinct()
        if collection_ids:
            queryset = queryset.filter(model_id__in=collection_ids)
        if price_ids:
            prices = Price.objects.filter(id__in=price_ids).order_by('from_price')
            if prices.exists():
                min_price = prices.first().from_price
                max_price = prices.last().to_price
                queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        serializer = GetCarpetModelsSerializer(queryset.distinct(), many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
