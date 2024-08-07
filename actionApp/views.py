from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg

from userApp.permissions import IsRegularUser
from .serializers import *


class BannersListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerDetailsAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class FavoriteListAPIView(ListAPIView):
    permission_classes = (IsRegularUser,)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # vazifa:
    #     - ordering_filter qo'shish: created_at, product_name

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class FavoritePostAPIView(APIView):
    permission_classes = [IsRegularUser]

    @swagger_auto_schema(
        request_body=FavoritePostSerializer,
    )
    def post(self, request):
        serializer = FavoritePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteRemoveAPIView(APIView):
    permission_classes = [IsRegularUser]

    def delete(self, request, pk):
        favorite = get_object_or_404(Favorite, pk=pk)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RateCreateAPIView(APIView):
    permission_classes = [IsRegularUser]

    @swagger_auto_schema(
        request_body=RatePostSerializer
    )
    def post(self, request):
        serializer = RatePostSerializer(data=request.data)
        if Rate.objects.filter(user=request.user, product_id=request.data['product']).exists():
            return Response({
                "success": False,
                "message": "This product already exists."
            }, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(user=request.user)
            product = get_object_or_404(Product, id=serializer.data['product'])
            avg_rating = Rate.objects.filter(product=product).aggregate(Avg('score'))
            product.rating = avg_rating.get('score__avg')
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
