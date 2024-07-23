from .models import Category, Product
from apps.account.models import User
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.


class CategoryListView(APIView):

    def get(self, request):

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Category successfully created"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(APIView):

    def get(self, request):

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            authorization_header = request.headers.get("Authorization")
            if authorization_header is None or not authorization_header.startswith(
                "Bearer "
            ):
                raise ValueError("Invalid Authorization header format")

            token = authorization_header.split(" ")[1]
            decoded_token = AccessToken(token)
            user_id = decoded_token.payload["user_id"]
            data = request.data
            data._mutable = True
            data["created_by"] = user_id
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Product successfully created"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
