from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .permissions import *

from .serializers import *


class UserRegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role='Regular')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPIView(APIView):
    permission_classes = [IsRegularUser]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserUpdateAPIView(APIView):
    permission_classes = [IsRegularUser]

    @swagger_auto_schema(
        request_body=UserUpdateSerializer
    )
    def put(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save(role='Regular')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    permission_classes = [IsRegularUser]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
