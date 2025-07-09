from rest_framework import serializers
from .models import Contact
from .utils import send_message_telegram
from .models import CHOICES_CITY


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'phone_number', 'city', 'address', 'comment']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        message = (
            f'project: SAG\n'
            f'client_id: {instance.id}\n'
            f'client_full_name: {instance.full_name}\n'
            f'client_phone_number: {instance.phone_number}\n'
            f'client_city: {dict(CHOICES_CITY).get(instance.city, 'Unknown')}\n'
            f'client_address: {instance.address}\n'
            f'client_comment: {instance.comment}\n'
        )
        send_message_telegram(message)
        return data