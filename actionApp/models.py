from django.db import models

from mainApp.models import Product
from userApp.models import User


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.user.username}: {self.product.name}"
