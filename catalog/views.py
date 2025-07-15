from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import (
    CarpetModel,
    Carpet,
    Shape,
    Color,
    Size,
    Room,
    Style,
    Catalog,
    Price,
)
from .serializers import (
    FilterSerializer,
    GetCatalogsSerializer,
    CarpetsSerializer,
    CarpetModelForSerializer,
    GetCarpetModelsSerializer,
    FilterForCarpetModelSerializer,
    StyleSerializer,
    RoomSerializer,
    ColorSerializer,
    ShapeSerializer,
    CollectionSerializer, GetPriceSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.translation import gettext_lazy as _


class CatalogViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Filter Choices For Catalog",
        operation_summary="Get Filter Choices For Catalog",
        responses={
            200: openapi.Response(
                description="Filter data for catalog",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'catalog': openapi.Schema(type=openapi.TYPE_OBJECT),
                        # simplified, or use ref to FilterSerializer
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
                        'labels': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        ),
                    },
                    required=['catalog', 'rooms', 'colors', 'shapes'],  # styles is optional
                )
            ),
            404: 'Catalog not found',
        },
        tags=['catalog']
    )
    def filter_choices(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if catalog is None:
            return Response(data={'error': _('Catalog not found')}, status=status.HTTP_404_NOT_FOUND)
        styles = Style.objects.filter(catalog=catalog)
        rooms = Room.objects.all()
        colors = Color.objects.all()
        shapes = Shape.objects.all()
        serializer = FilterSerializer(catalog, context={'request': request})

        response_data = {
            'catalog': serializer.data,
            'rooms': RoomSerializer(rooms, many=True, context={'request': request}).data,
            'colors': ColorSerializer(colors, many=True, context={'request': request}).data,
            'shapes': ShapeSerializer(shapes, many=True, context={'request': request}).data,
        }
        if styles.exists():
            response_data['styles'] = StyleSerializer(styles, many=True, context={'request': request}).data,

        response_data['labels'] = {
            'catalog': _('Catalog'),
            'rooms': _('Rooms'),
            'colors': _('Colors'),
            'shapes': _('Shapes'),
            'styles': _('Styles'),
        }
        return Response(data=response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Filter Choices For Collections",
        operation_summary="Get Filter Choices For Collections",
        responses={
            200: openapi.Response(
                description="Filter data for catalog",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'catalog': openapi.Schema(type=openapi.TYPE_OBJECT),
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
        tags=['catalog']
    )
    def filter_choices_for_carpet_model(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()

        if catalog is None:
            return Response(data={'error': _('Catalog not found')}, status=status.HTTP_404_NOT_FOUND)

        collections = Carpet.objects.filter(catalog=catalog)
        styles = Style.objects.filter(catalog=catalog)
        rooms = Room.objects.all()
        colors = Color.objects.all()
        shapes = Shape.objects.all()
        prices = Price.objects.all()

        serializer = FilterSerializer(catalog, context={'request': request})

        response_data = {
            'catalog': serializer.data,
            'collections': CollectionSerializer(collections, many=True, context={'request': request}).data,
            'rooms': RoomSerializer(rooms, many=True, context={'request': request}).data,
            'colors': ColorSerializer(colors, many=True, context={'request': request}).data,
            'shapes': ShapeSerializer(shapes, many=True, context={'request': request}).data,
            'prices': GetPriceSerializer(prices, many=True, context={'request': request}).data,
        }

        if styles.exists():
            response_data['styles'] = StyleSerializer(styles, many=True, context={'request': request}).da
        response_data['labels'] = {
            'catalog': _('Catalog'),
            'collections': _('Collections'),
            'rooms': _('Rooms'),
            'colors': _('Colors'),
            'shapes': _('Shapes'),
            'styles': _('Styles'),
            'prices': _('Prices'),
        }

        return Response(data=response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Catalogs",
        operation_summary="Get Catalogs",
        responses={
            200: GetCatalogsSerializer(),
        },
        tags=['catalog']
    )
    def get_catalogs(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        serializer = GetCatalogsSerializer(catalogs, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Carpets By Catalog Id",
        operation_summary="Get Carpets By Catalog Id ",
        responses={
            200: CarpetsSerializer(),
        },
        tags=['catalog']
    )
    def get_carpets_by_catalog_id(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if catalog is None:
            return Response(data={'error': _('Catalog not found')}, status=status.HTTP_404_NOT_FOUND)
        all_carpets = Carpet.objects.filter(catalog=catalog)
        serializer = CarpetsSerializer(all_carpets, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Carpet Models By Carpet Id",
        operation_summary="Get Carpet Models By Carpet Id",
        responses={
            200: GetCarpetModelsSerializer(),
        },
        tags=['catalog']
    )
    def get_carpet_models_by_carpet_id(self, request, *args, **kwargs):
        carpet = Carpet.objects.filter(id=kwargs['pk']).first()
        if carpet is None:
            return Response(data={'error': _('Carpet not found')}, status=status.HTTP_404_NOT_FOUND)
        all_carpet_models = CarpetModel.objects.filter(model=carpet)
        serializer = GetCarpetModelsSerializer(all_carpet_models, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Filter and Sort For Carpet",
        operation_summary="Filter and Sort For Carpet",
        manual_parameters=[
            openapi.Parameter(
                'sort_by', openapi.IN_QUERY, description="1=New, 2=Hit, 3=Sale",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'styles', openapi.IN_QUERY,
                description='Comma-separated list of style IDs', type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'collections', openapi.IN_QUERY,
                description='Comma-separated list of style IDs', type=openapi.TYPE_STRING
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
                description='Comma-separated list of shape IDs', type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: CarpetsSerializer(),
        },
        tags=['catalog']
    )
    def filter_and_sort_carpets_for_carpet_model(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if not catalog:
            return Response(data={'error': _('Catalog not found')}, status=status.HTTP_404_NOT_FOUND)

        data = request.GET
        sort_by = data.get('sort_by')

        # Initial queryset: now we work directly with CarpetModel
        carpet_model_filter = CarpetModel.objects.filter(catalog=catalog)

        if sort_by == "1":
            carpet_model_filter = carpet_model_filter.filter(collection_type=2)
        elif sort_by == "2":
            carpet_model_filter = carpet_model_filter.filter(collection_type=4)
        elif sort_by == "3":
            carpet_model_filter = carpet_model_filter.filter(collection_type=3)

        def get_list(param):
            return [int(x) for x in request.GET.get(param, "").split(",") if x.strip().isdigit()]

        # Extracting filter params
        collection_ids = get_list("collections")
        style_ids = get_list("styles")
        room_ids = get_list("rooms")
        color_ids = get_list("colors")
        shape_ids = get_list("shapes")
        price_ids = get_list("price")

        if style_ids:
            carpet_model_filter = carpet_model_filter.filter(style_id__in=style_ids)

        if room_ids:
            carpet_model_filter = carpet_model_filter.filter(room_id__in=room_ids)

        if color_ids:
            carpet_model_filter = carpet_model_filter.filter(color_id__in=color_ids)

        if shape_ids:
            carpet_model_filter = carpet_model_filter.filter(size__shape_id__in=shape_ids).distinct()

        if collection_ids:
            carpet_model_filter = carpet_model_filter.filter(model_id__in=collection_ids)

        if price_ids:
            prices = Price.objects.filter(id__in=price_ids).order_by('from_price')
            if prices.exists():
                min_price = prices.first().from_price
                max_price = prices.last().to_price
                carpet_model_filter = carpet_model_filter.filter(price__gte=min_price, price__lte=max_price)

        serializer = GetCarpetModelsSerializer(carpet_model_filter.distinct(), many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Filter and Sort For Carpet",
        operation_summary="Filter and Sort For Carpet",
        manual_parameters=[
            openapi.Parameter(
                'sort_by', openapi.IN_QUERY, description="1=New, 2=Hit, 3=Sale",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'styles', openapi.IN_QUERY,
                description='Comma-separated list of style IDs', type=openapi.TYPE_STRING
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
            )
        ],
        responses={
            200: CarpetsSerializer(),
        },
        tags=['catalog']
    )
    def filter_and_sort_carpets(self, request, *args, **kwargs):
        catalog = Catalog.objects.filter(id=kwargs['pk']).first()
        if not catalog:
            return Response(data={'error': _('Catalog not found')}, status=status.HTTP_404_NOT_FOUND)

        data = request.GET

        def get_list(param):
            return [int(x) for x in request.GET.get(param, "").split(",") if x.strip().isdigit()]

        # Extracting filter params
        style_ids = get_list("styles")
        room_ids = get_list("rooms")
        color_ids = get_list("colors")
        shape_ids = get_list("shapes")

        # Filter CarpetModel
        carpet_model_filter = CarpetModel.objects.filter(catalog=catalog)

        if style_ids:
            carpet_model_filter = carpet_model_filter.filter(style_id__in=style_ids)

        if room_ids:
            carpet_model_filter = carpet_model_filter.filter(room_id__in=room_ids)

        if color_ids:
            carpet_model_filter = carpet_model_filter.filter(color_id__in=color_ids)

        if shape_ids:
            carpet_model_filter = carpet_model_filter.filter(size__shape_id__in=shape_ids).distinct()

        model_ids = carpet_model_filter.values_list('model_id', flat=True).distinct()

        # Endi faqat shu model_id lar bilan ishlaymiz
        queryset = Carpet.objects.filter(catalog=catalog, id__in=model_ids)

        # sort_by = 1 (New), 2 (Hit), 3 (Sale)
        try:
            sort_by = int(data.get('sort_by', 0))
        except ValueError:
            sort_by = 0

        if sort_by == 1:
            queryset = queryset.filter(collection_type=2)
        elif sort_by == 2:
            queryset = queryset.filter(collection_type=4)
        elif sort_by == 3:
            queryset = queryset.filter(collection_type=3)

        serializer = CarpetsSerializer(queryset.distinct(), many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Get Carpet Model By Id",
        operation_summary="Get Carpet Model By Id",
        responses={
            200: CarpetModelForSerializer(),
        },
        tags=['catalog']
    )
    def get_carpet_model_by_id(self, request, *args, **kwargs):
        carpet_model = CarpetModel.objects.filter(id=kwargs['pk']).first()
        if carpet_model is None:
            return Response(data={'error': _('Carpet Model not found')}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarpetModelForSerializer(carpet_model, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
