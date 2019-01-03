import string
import random

from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    token = models.CharField(max_length=10, unique=True)

    @staticmethod
    def generate_random_token():
        code = [random.choice(string.digits) for _ in range(10)]
        code = ''.join(code)
        return code


        # class Address(models.Model):
        #    Account = models.ForeignKey()
