from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product
from .models import Purchase, PurchaseItem


@login_required
def add_item_to_cart(request, product_id):
    amount = int(request.POST.get('amount', 0))
    print (amount)

    try:
        purchase = Purchase.objects.get(user=request.user, state='N')
    except Purchase.DoesNotExist:
        purchase = Purchase.objects.create(user=request.user, state='N')

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    try:
        purchase_item = PurchaseItem.objects.get(purchase=purchase,
                                                 product=product)
    except PurchaseItem.DoesNotExist:
        purchase_item = PurchaseItem.objects.create(purchase=purchase,
                                                    product=product,
                                                    amount=0,
                                                    fee=product.price)
    purchase_item.amount += amount
    purchase_item.fee = product.price
    purchase_item.save()

    return HttpResponse("amme")


@login_required
def show_cart(request):
    try:
        purchase = Purchase.objects.get(user=request.user, state='N')
    except Purchase.DoesNotExist:
        return render(request, 'purchase/cart.html', {
            'items': []
        })

    purchase_items = []
    for p in PurchaseItem.objects.filter(purchase=purchase):
        purchase_items.append({
            'name': p.product.name,
            'amount': p.amount,
            'fee': p.fee
        })

    return render(request, 'purchase/cart.html', {
        'items': purchase_items
    })

