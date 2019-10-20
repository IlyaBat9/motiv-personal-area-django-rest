from rest_framework import serializers

from .models import Tariff


class TariffSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'price': instance.price,
            'description': instance.description,
            'minutes': instance.minutes,
            'sms': instance.sms,
            'traffic': round((instance.traffic//1024)/1024, 1)
        }

    class Meta:
        model = Tariff
        fields = '__all__'
