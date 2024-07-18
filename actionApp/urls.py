from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannersListAPIView.as_view()),
    path('banners/<int:pk>/details/', BannerDetailsAPIView.as_view()),

    path('my-favorites/', FavoriteListAPIView.as_view()),
    path('add-favorite/', FavoritePostAPIView.as_view()),
    path('remove-favorite/<int:pk>/', FavoriteRemoveAPIView.as_view()),
]
