from .models import Category, Product
from apps.account.models import User
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from elasticsearch_dsl.query import MultiMatch
from apps.product.document import ProductDocument
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView


class MainPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CategoryListView(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MainPagination


class ProductListView(APIView):

    pagination_class = MainPagination

    def get(self, request):
        filter_params = {}
        elasticsearch_resp = request.query_params.get("elasticsearch")
        if elasticsearch_resp:
            search_query = MultiMatch(
                query=elasticsearch_resp,
                fields=["title", "description"],
                fuzziness="AUTO",
            )
            products = (
                ProductDocument.search()
                .query(search_query)
                .to_queryset()
                .order_by("-created_at")
            )
            if products:
                serializer = ProductSerializer(products, many=True)
                paginator = MainPagination()
                result_page = paginator.paginate_queryset(products, request)
                return paginator.get_paginated_response(
                    serializer.data
                )
            else:
                return Response(
                    {"message": "No product found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        category_id = request.query_params.get("category_id")
        if category_id:
            filter_params["category_id"] = category_id

        search = request.query_params.get("search")
        if search:
            filter_params["title__icontains"] = search

        if filter_params:
            products = Product.objects.filter(**filter_params).order_by("-created_at")
        else:
            products = Product.objects.all().order_by("-created_at")

        paginator = MainPagination()
        result_page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(
            serializer.data
        )

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


class ProductDetailView(APIView):

    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, product_id):

        try:
            authorization_header = request.headers.get("Authorization")
            if authorization_header is None or not authorization_header.startswith(
                "Bearer "
            ):
                raise ValueError("Invalid Authorization header format")

            token = authorization_header.split(" ")[1]
            decoded_token = AccessToken(token)
            user_id = decoded_token.payload["user_id"]
            user = User.objects.get(id=user_id)
            if user.is_staff is False:
                return Response(
                    {"message": "You do not have permission to perform this action"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            product = Product.objects.get(id=product_id)
            data = request.data
            data._mutable = True
            if data.get("created_by"):
                data.pop("created_by")

            serializer = ProductSerializer(product, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Product successfully updated"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, product_id):

        try:
            authorization_header = request.headers.get("Authorization")
            if authorization_header is None or not authorization_header.startswith(
                "Bearer "
            ):
                raise ValueError("Invalid Authorization header format")

            token = authorization_header.split(" ")[1]
            decoded_token = AccessToken(token)
            user_id = decoded_token.payload["user_id"]
            user = User.objects.get(id=user_id)
            if user.is_staff is False:
                return Response(
                    {"message": "You do not have permission to perform this action"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response(
                {"message": "Product successfully deleted"},
                status=status.HTTP_200_OK,
            )
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CategoryDetailView(APIView):

    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, category_id):

        try:
            category = Category.objects.get(id=category_id)
            data = request.data
            serializer = CategorySerializer(category, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Category successfully updated"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, category_id):

        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return Response(
                {"message": "Category successfully deleted"},
                status=status.HTTP_200_OK,
            )
        except Category.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
