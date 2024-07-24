from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from apps.account.models import User
from apps.account.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserView(APIView):
    def get(self, request):
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
            serializer = UserSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
            user = User.objects.get(id=user_id)
            data = request.data
            serializer = UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "User successfully updated"}, status=status.HTTP_200_OK
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return Response(
            {"message": "User deleted successfully"}, status=status.HTTP_200_OK
        )


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            access_token = AccessToken.for_user(serializer.instance)
            refresh_token = RefreshToken.for_user(serializer.instance)
            return Response(
                {
                    "access_token": str(access_token),
                    "refresh_token": str(refresh_token),
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
