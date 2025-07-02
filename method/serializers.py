from rest_framework import serializers
from .models import (
    Content,
    Material,
    ProductGallery, AboutMethod,
)
from django.conf import settings


class GetContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'image', 'icon']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class GetMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'image']


class GetProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['id', 'image']


class AboutMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMethod
        fields = ['id', 'title', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data