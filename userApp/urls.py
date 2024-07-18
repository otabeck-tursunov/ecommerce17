from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    path('register/', UserRegisterAPIView.as_view()),
    path('me/', UserDetailsAPIView.as_view()),
    path('me/update/', UserUpdateAPIView.as_view()),
    path('me/delete/', UserDeleteAPIView.as_view()),
]
