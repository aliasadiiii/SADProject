from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    is_available = models.BooleanField()
    photo = models.ImageField(upload_to='products/')
    expires_at = models.DateField()
