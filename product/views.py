from django.shortcuts import render

from .models import Product


def product_list(request):
    kinds = Product.objects.all().values_list(
        'kind', flat=True)

    queryset = Product.objects.all()
    if request.GET.get('kind') is not None:
        queryset = queryset.filter(kind=request.GET.get('kind'))

    products = []
    for p in queryset:
        products.append({
            'name': p.name,
            'price': p.price,
            'is_available': p.is_available,
            'photo': p.photo
        })

    return render(request, 'list.html',
                  context={'products': products, 'kinds': list(kinds)})
