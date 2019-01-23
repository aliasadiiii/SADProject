from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class Purchase(models.Model):
    STATE_CHOICES = (
        ('N', 'New'),
        ('C', 'Cancelled'),
        ('D', 'Done')
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='N')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    fee = models.IntegerField()
