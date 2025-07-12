from rest_framework import serializers
from .models import Header, Questions, Collection
from catalog.models import Catalog, Style, CarpetModel, Carpet
from blog.models import Blog
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'image']


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


class CatalogSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'styles', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class GetBlogSerializer(serializers.ModelSerializer):
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


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['question'] = getattr(instance, f'question_{lang}')
            data['answer'] = getattr(instance, f'answer_{lang}')
        return data


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'collection', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['collection'] = instance.get_collection_display()
        return data


class CarpetSerializer(serializers.ModelSerializer):
    collection = serializers.SerializerMethodField()

    class Meta:
        model = Carpet
        fields = ['id', 'name', 'image', 'collection']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data

    def get_collection(self, obj):
        return _('collection')


class CarpetModelSerializer(serializers.ModelSerializer):
    model = serializers.SerializerMethodField()
    class Meta:
        model = CarpetModel
        fields = ['id', 'name', 'image', 'model']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.discount > 0:
            data['price'] = instance.discount
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data

    def get_model(self, obj):
        return _('carpet_model')
