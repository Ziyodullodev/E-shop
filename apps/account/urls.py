from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from apps.account.views import UserView, RegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('user/', UserView.as_view(), name='user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
]