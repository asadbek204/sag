from rest_framework import serializers
from .models import Room, RoomImage
from django.conf import settings


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data


class GetRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'room', 'name', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['room'] = getattr(instance.room, f'name_{lang}')
        return data