import string
import random

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models


def phone_validator(phone):
    if len(phone) != 11 or not str(phone).isalnum():
        raise ValidationError("{} is not a phone number".format(phone))


class Account(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, validators=[phone_validator])
    address = models.CharField(max_length=200,null=True,blank=True)
    activation_token = models.CharField(max_length=10, unique=True)
    forget_password_token = models.CharField(max_length=10, unique=True,
                                             null=True)
    avatar = models.ImageField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{username} _ {name}'.format(username=self.user.username,
                                            name=self.name)

    @staticmethod
    def generate_random_token():
        code = [random.choice(string.digits) for _ in range(10)]
        code = ''.join(code)
        return code
