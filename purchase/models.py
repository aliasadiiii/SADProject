from django.db import models

# Create your models here.
from product.models import Product


class Cart(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    fee = models.IntegerField()
