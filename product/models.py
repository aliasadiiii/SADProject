from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    is_available = models.BooleanField() 
    photo = models.ImageField(upload_to='products/')
