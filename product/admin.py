from django.contrib import admin
from .models import Product, ProductKind

admin.site.register(Product)
admin.site.register(ProductKind)
