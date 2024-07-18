from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import *


class CategoriesAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='title',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by Title',
            )
        ]
    )
    def get(self, request):
        categories = Category.objects.all()

        title_search = request.query_params.get('title')

        if title_search is not None:
            categories = categories.filter(title__icontains=title_search)

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailsAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class SubCategoriesAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Filter by Category ID"),
            openapi.Parameter(
                name='title',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by Title"
            )
        ]
    )
    def get(self, request):
        subCategories = SubCategory.objects.all()

        category_filter = request.query_params.get('category', None)
        title_search = request.query_params.get('title', None)

        if category_filter is not None:
            subCategories = subCategories.filter(category__id=category_filter)

        if title_search is not None:
            subCategories = subCategories.filter(title__icontains=title_search)

        serializer = SubCategorySerializer(subCategories, many=True)
        return Response(serializer.data)


class SubCategoryDetailsAPIView(APIView):
    def get(self, request, subCategory_id):
        subCategory = get_object_or_404(SubCategory, id=subCategory_id)
        serializer = SubCategorySerializer(subCategory)
        return Response(serializer.data)


# Product
class ProductsAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Filter by Category ID"
            ),
            openapi.Parameter(
                name='subCategory',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Filter by SubCategory ID"
            ),
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by Name"
            ),
            openapi.Parameter(
                name='brand',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by brand"
            ),
            openapi.Parameter(
                name='min_price',
                in_=openapi.IN_QUERY,
                type=openapi.FORMAT_FLOAT,
                description="Filter by min price"
            ),
            openapi.Parameter(
                name='max_price',
                in_=openapi.IN_QUERY,
                type=openapi.FORMAT_FLOAT,
                description="Filter by max price"
            ),
            openapi.Parameter(
                name='order_by',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Order by Minimum Price, Maximum Price, Discount, Ordered, Rating, Firs Create, Last Create",
                enum=['price_min', 'price_max', 'discount', 'ordered', 'rating', 'created_at_first', 'created_at_last']
            )
        ]
    )
    def get(self, request):
        products = Product.objects.all()

        subCategory_filter = request.query_params.get('subCategory', None)
        if subCategory_filter is not None:
            products = products.filter(subCategory_id=subCategory_filter)

        cateogry_filter = request.query_params.get('category', None)
        if cateogry_filter is not None:
            products = products.filter(subCategory__category_id=cateogry_filter)

        name_search = request.query_params.get('name', None)
        if name_search is not None:
            products = products.filter(name__icontains=name_search)

        brand_search = request.query_params.get('brand', None)
        if brand_search is not None:
            products = products.filter(brand__icontains=brand_search)

        min_price = request.query_params.get('min_price', None)
        if min_price is not None:
            products = products.filter(price__gte=min_price)

        max_price = request.query_params.get('max_price', None)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

        order_by = request.query_params.get('order_by', None)
        if order_by is not None:
            if order_by == 'price_min':
                products = products.order_by('price')
            elif order_by == 'price_max':
                products = products.order_by('-price')
            elif order_by == 'discount':
                products = products.order_by('-discount')
            elif order_by == 'ordered':
                products = products.order_by('-ordered')
            elif order_by == 'rating':
                products = products.order_by('-rating')
            elif order_by == 'created_at_first':
                products = products.order_by('created_at')
            elif order_by == 'created_at_last':
                products = products.order_by('-created_at')

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailsAPIView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
