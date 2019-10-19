from rest_framework import serializers
from .models import Profile


class UserBaseInfoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            "number": instance.user.username,
            "full_name": instance.get_full_name(),
            "first_name": instance.first_name,
            "last_name": instance.second_name,
            "middle_name": instance.middle_name,
        }

    class Meta:
        model = Profile
        fields = "__all__"

