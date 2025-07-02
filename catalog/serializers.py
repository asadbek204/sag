from rest_framework import serializers
from .models import (
    Style,
    Room,
    Color,
    Shape,
    Catalog,
    Carpet,
    Price,
    CarpetModel,
    Size, CarpetModelImages,
)
from django.conf import settings


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class PriceSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Price
        filter = ['id', 'price']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = f'{instance.from_price} {instance.to_price}'
        return data


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class FilterForCarpetModelSerializer(serializers.ModelSerializer):
    collections = serializers.SerializerMethodField()
    styles = serializers.SerializerMethodField()
    rooms = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    shapes = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'collections', 'styles', 'rooms', 'colors', 'shapes']

    def get_collections(self, obj):
        collections = Carpet.objects.filter(catalog=obj)
        return CollectionSerializer(collections, many=True).data

    def get_styles(self, obj):
        styles = Style.objects.filter(catalog=obj)
        if styles:
            return StyleSerializer(styles, many=True).data
        return None

    def get_rooms(self, obj):
        rooms = Room.objects.all()
        return RoomSerializer(rooms, many=True).data

    def get_colors(self, obj):
        colors = Room.objects.all()
        return ColorSerializer(colors, many=True).data

    def get_shapes(self, obj):
        shapes = Room.objects.all()
        return ShapeSerializer(shapes, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class GetCatalogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class CarpetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = ['id', 'catalog', 'name', 'image', 'collection_type']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['collection_type'] = instance.get_collection_type_display()
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['catalog'] = getattr(instance.catalog, f'name_{lang}')
        return data


class GetCarpetModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetModel
        fields = ['id', 'name', 'image', 'color', 'collection_type', 'model', 'price']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['collection_type'] = instance.get_collection_type_display()
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['model'] = getattr(instance.model, f'name_{lang}')
            data['color'] = getattr(instance.color, f'name_{lang}')
        return data


class ShapeForCarpetModelSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Size
        fields = ['id', 'shape', 'size', 'price', 'discount']

    def get_size(self, obj):
        return f'{obj.width} x {obj.length}'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.discount == 0:
            data.pop('discount', None)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['shape'] = getattr(instance.shape, f'name_{lang}')
        return data


class CarpetModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetModelImages
        fields = ['id', 'image']


class CarpetModelImageForSerializer(serializers.SerializerMethodField):
    class Meta:
        model = CarpetModel
        fields = ['id', 'image']


class CarpetModelForSerializer(serializers.ModelSerializer):
    shapes = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = CarpetModel
        fields = ['id', 'name', 'color', 'image', 'shapes', 'images']

    def get_shapes(self, obj):
        sizes = Size.objects.filter(carpet_model=obj).select_related('shape')
        shape_map = {}

        for size in sizes:
            shape_name = size.shape.name
            serialized = ShapeForCarpetModelSerializer(size, context=self.context).data
            shape_map.setdefault(shape_name, []).append(serialized)

        return shape_map

    def get_images(self, obj):
        request = self.context.get('request')
        images = CarpetModelImages.objects.filter(carpet_model=obj)
        return CarpetModelImageSerializer(images, many=True, context={'request': request}).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['color'] = getattr(instance.color, f'name_{lang}')
        return data


class DiscountedCarpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = ['id', 'name', 'image', 'collection_type']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['collection_type'] = instance.get_collection_type_display()
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class DiscountedCarpetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpetModel
        fields = ['id', 'name', 'image', 'collection_type']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['collection_type'] = instance.get_collection_type_display()
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data
