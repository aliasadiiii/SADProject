import string
import random

from django.contrib.auth.models import User
from django.db import models

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
    address = models.CharField(max_length=200, null=True, blank=True)
    locationX = models.CharField(max_length=100,null=True,blank=True)
    locationY = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    reference_token = models.CharField(max_length=10, unique=True,
                                       default=generate_random_token)

    def __init__(self, *args, **kwargs):
        super(Purchase, self).__init__(*args, **kwargs)
        self.__original_state = self.state

    def __str__(self):
        return "Purchase #{}".format(self.reference_token)

    def save(self, *args, **kwargs):
        if self.__original_state != self.state:
            from .utils import send_purchase_state_change_email
            send_purchase_state_change_email(self)
        super(Purchase, self).save(*args, **kwargs)
        self.__original_state = self.state


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    fee = models.IntegerField()
