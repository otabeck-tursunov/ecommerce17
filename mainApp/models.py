from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=75)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.category.title}: {self.title}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=50, blank=True, null=True)
    seller = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    discount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    guaranty = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=3000)
    country = models.CharField(max_length=50, blank=True, null=True)
    amount = models.PositiveSmallIntegerField(default=1)
    ordered = models.PositiveIntegerField(default=0)
    rated = models.PositiveIntegerField(default=0)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Property(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=255)
    important = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
