import string
import random

from django.contrib.auth.models import User
from django.db import models

from account.models import Address
from product.models import Product


def generate_random_token():
    code = [random.choice(string.digits) for _ in range(10)]
    code = ''.join(code)
    return code


class Purchase(models.Model):
    STATE_CHOICES = (
        ('N', 'New'),
        ('I', 'In Review'),
        ('C', 'Cancelled'),
        ('D', 'Done')
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='N')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    reference_token = models.CharField(max_length=10, unique=True,
                                       default=generate_random_token)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    fee = models.IntegerField()
