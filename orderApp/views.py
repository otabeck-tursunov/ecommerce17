from rest_framework.generics import *

from datetime import date, timedelta

from userApp.permissions import IsRegularUser
from .serializers import *
from .models import *


class CartItemCreateAPIView(CreateAPIView):
    permission_classes = (IsRegularUser,)

    queryset = CartItem.objects.all()
    serializer_class = CartItemPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemsListAPIView(ListAPIView):
    permission_classes = (IsRegularUser,)

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        queryset = CartItem.objects.filter(user=self.request.user)
        return queryset


class CartItemDestroyAPIView(DestroyAPIView):
    permission_classes = (IsRegularUser,)

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        cart_item = get_object_or_404(CartItem, user=self.request.user, id=self.kwargs['pk'])
        return cart_item


class CartItemUpdateAPIView(UpdateAPIView):
    permission_classes = (IsRegularUser,)

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        cart_item = get_object_or_404(CartItem, user=self.request.user, id=self.kwargs['pk'])
        return cart_item


class OrderListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsRegularUser,)

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderPostSerializer

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        cart_items = CartItem.objects.filter(user=self.request.user)
        if cart_items.exists():

            today = date.today()
            delivery_date = today + timedelta(days=1)

            summa = 0
            for item in cart_items:
                summa += item.product.price * item.amount * (1 - item.product.discount / 100)

            order = serializer.save(
                user=self.request.user,
                delivery_date=delivery_date,
                total_payment=summa,
            )

            for cart_item in cart_items:
                OrderItem.objects.create(
                    product=cart_item.product,
                    amount=cart_item.amount,
                    user=self.request.user,
                    order=order
                )
            cart_items.delete()
