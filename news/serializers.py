from rest_framework import serializers

from blog.models import SocialMediaIcon
from .models import News, NewsSocialMediaLink
from django.conf import settings


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
        return data


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaIcon
        fields = ['name', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class LinkSerializer(serializers.ModelSerializer):
    icon = IconSerializer()
    class Meta:
        model = NewsSocialMediaLink
        fields = ['id', 'icon', 'link']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['icon'] = getattr(instance.icon, f'name_{lang}')
        return data


class GetNewsSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image', 'view_count', 'links', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data

    def get_links(self, obj):
        request = self.context.get('request')
        links = NewsSocialMediaLink.objects.filter(news=obj)
        return LinkSerializer(links, many=True, context={'request': request}).data