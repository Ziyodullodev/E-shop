from rest_framework import serializers
from apps.account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
