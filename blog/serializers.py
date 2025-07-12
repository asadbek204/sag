from rest_framework import serializers
from .models import Blog, BlogSocialMediaLink, SocialMediaIcon
from django.conf import settings
from news.serializers import IconSerializer


class AllBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'content', 'title']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
        return data


class BlogLinkSerializer(serializers.ModelSerializer):
    icon = IconSerializer()
    class Meta:
        model = BlogSocialMediaLink
        fields = ['id', 'icon', 'link']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['icon'] = getattr(instance.icon, f'name_{lang}')
        return data


class BlogDetailSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'description', 'created_at', 'links', 'view_count']

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
        links = BlogSocialMediaLink.objects.filter(blog=obj)
        return BlogLinkSerializer(links, many=True, context={'request': request}).data