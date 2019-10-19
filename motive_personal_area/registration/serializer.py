from rest_framework import serializers
from django.utils import timezone
from re import match
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
