from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ChangePasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class LoginOTPSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=5)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass