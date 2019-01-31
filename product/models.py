from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    kind = models.ForeignKey('ProductKind', on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    is_available = models.BooleanField()
    photo = models.ImageField(upload_to='products/')
    expires_at = models.DateField()
    manufacture_date = models.DateField()

    def __str__(self):
        return self.name


class ProductKind(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    author = models.ForeignKey('account.Account', on_delete=models.PROTECT)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()
