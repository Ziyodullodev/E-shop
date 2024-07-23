from rest_framework.serializers import ModelSerializer
from apps.account.models import User
from apps.product.models import Product, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")

class ProductDetailSerializer(ModelSerializer):
    category = CategorySerializer()
    created_by = UserSerializer()

    class Meta:
        model = Product
        fields = "__all__"