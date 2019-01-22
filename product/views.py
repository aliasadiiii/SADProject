import jdatetime
from datetime import date

from django.shortcuts import render

from .models import Product


def product_list(request):
    kinds = Product.objects.all().values_list(
        'kind__name', flat=True)

    queryset = Product.objects.filter(expires_at__gt=date.today())
    if request.GET.get('kind') is not None:
        queryset = queryset.filter(kind__name=request.GET.get('kind'))

    products = []
    for p in queryset:
        products.append({
            'name': p.name,
            'price': p.price,
            'is_available': p.is_available,
            'expires_at': jdatetime.date.fromgregorian(date=p.expires_at),
            'manufacture_date': jdatetime.date.fromgregorian(
                date=p.manufacture_date),
            'photo': p.photo,
            'product_id': p.id
        })

    return render(request, 'list.html',
                  context={'products': products, 'kinds': list(set(kinds))})


def product_page(request, product_id):
    queryset = Product.objects.get(id=product_id)
    p = queryset
    product = {'name': p.name,
            'price': p.price,
            'is_available': p.is_available,
            'expires_at': jdatetime.date.fromgregorian(date=p.expires_at),
            'manufacture_date': jdatetime.date.fromgregorian(
                date=p.manufacture_date),
            'photo': p.photo,
            'product_id': p.id}
    return render(request, 'product_page.html',
                  context={'product': product},)
    # print(product_id)


