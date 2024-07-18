from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'gender', 'birth_date',
            'address', 'last_login', 'date_joined'
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'phone_number'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'max_length': 15},
            'email': {'required': False},
            'phone_number': {'required': False},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'password', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'gender',
            'birth_date', 'address'
        )

        extra_kwargs = {
            'password': {'write_only': True},
        }
