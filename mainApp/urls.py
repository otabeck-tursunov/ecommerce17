from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view()),
    path('categories/<int:category_id>/details/', CategoryDetailsAPIView.as_view()),

    path('subCategories/', SubCategoriesAPIView.as_view()),
    path('subCategories/<int:subCategory_id>/details/', SubCategoryDetailsAPIView.as_view()),

    path('products/', ProductsAPIView.as_view()),
    path('products/<int:product_id>/details/', ProductDetailsAPIView.as_view()),
]
