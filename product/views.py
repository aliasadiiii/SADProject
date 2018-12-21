from django.core import serializers
from django.shortcuts import render

from .models import Product


def product_list(request):
    products = []
    for p in Product.objects.all():
        print (p.photo)
        products.append({
            'name': p.name,
            'price': p.price,
            'is_available': p.is_available,
            'photo': p.photo
        })

    return render(request, 'list.html', context={'products': products})
