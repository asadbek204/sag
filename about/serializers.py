from rest_framework import serializers
from .models import (
    AboutCompany,
    BriefAbout,
    ProductionVolume,
    Gallery,
    AboutProduction,
)
from django.conf import settings


class GetAboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ['id', 'image', 'title']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
        return data


class GetBriefAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefAbout
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


class GetProductionVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionVolume
        fields = ['id', 'year', 'volume']


class GetGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image']


class GetAboutProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProduction
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