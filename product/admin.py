from django.contrib import admin
from .models import Product, ProductKind, Comment

admin.site.register(Product)
admin.site.register(ProductKind)
admin.site.register(Comment)
