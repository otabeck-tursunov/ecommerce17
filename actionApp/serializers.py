from rest_framework import serializers

from mainApp.serializers import ProductSerializer
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ProductCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount')

        # vazifa


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductCascadeSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'created_at')


class FavoritePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'product', 'created_at')