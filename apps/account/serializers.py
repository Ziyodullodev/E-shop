from rest_framework.serializers import ModelSerializer
from apps.account.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}
        required_fields = ['email', 'password', 'first_name', 'last_name']
