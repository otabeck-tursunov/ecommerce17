from rest_framework import serializers
from .models import *


class CartItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('product', 'amount')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'amount')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        order = super(OrderSerializer, self).to_representation(instance)

        order_items = OrderItem.objects.filter(order=instance)
        serializer = OrderItemSerializer(order_items, many=True)

        order.update(
            {
                'order_items': serializer.data
            }
        )
        return order


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        extra_kwargs = {
            'user': {'required': False},
            'total_payment': {'required': False},
            'delivery_date': {'required': False},
            'status': {'required': False},
        }
