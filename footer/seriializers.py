from .models import CallCenter, SocialMedia
from rest_framework import serializers


class CallCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallCenter
        fields = ['id', 'phone_number']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'image', 'url']