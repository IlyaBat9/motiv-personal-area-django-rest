from rest_framework import serializers

from .models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        minutes = instance.minutes.minute + instance.minutes.hour*60
        return {
            'money': instance.money,
            'minutes': minutes,
            'sms': instance.sms,
            'traffic': round((instance.traffic//1024)/1024, 1)
        }

    class Meta:
        model = Balance
        fields = '__all__'
