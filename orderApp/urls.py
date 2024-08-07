from django.urls import path
from .views import *

urlpatterns = [
    path('cart-items/', CartItemsListAPIView.as_view()),
    path('cart-items/create/', CartItemCreateAPIView.as_view()),
    path('cart-items/<int:pk>/delete/', CartItemDestroyAPIView.as_view()),
    path('cart-items/<int:pk>/update/', CartItemUpdateAPIView.as_view()),

    path('orders/', OrderListCreateAPIView.as_view()),
]
