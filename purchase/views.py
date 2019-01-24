from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View

from product.models import Product
from .forms import EditPurchaseItemForm
from .models import Purchase, PurchaseItem


@login_required
def add_item_to_purchase(request, product_id):
    amount = int(request.POST.get('amount', 0))

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

    return redirect(reverse('product_list'))


@login_required
def show_purchase(request):
    try:
        purchase = Purchase.objects.get(user=request.user, state='N')
    except Purchase.DoesNotExist:
        return render(request, 'purchase/purchase.html', {
            'items': []
        })

    purchase_items = []
    for p in PurchaseItem.objects.filter(purchase=purchase):
        purchase_items.append({
            'purchase_item_id': p.id,
            'name': p.product.name,
            'amount': p.amount,
            'fee': p.fee
        })

    return render(request, 'purchase/purchase.html', {
        'items': purchase_items
    })


class EditPurchaseItemView(View):
    @staticmethod
    def get(request, purchase_item_id):
        try:
            purchase_item = PurchaseItem.objects.get(id=purchase_item_id)
        except PurchaseItem.DoesNotExist:
            return HttpResponse(status=404)

        form = EditPurchaseItemForm(instance=purchase_item)
        return render(request, 'purchase/edit_purchase_item.html',
                      {
                          'form': form,
                          'purchase_item': {
                              'id': purchase_item.id,
                              'name': purchase_item.product.name,
                      }})

    @staticmethod
    def post(request, purchase_item_id):
        try:
            purchase_item = PurchaseItem.objects.get(id=purchase_item_id)
        except PurchaseItem.DoesNotExist:
            return HttpResponse(status=404)

        form = EditPurchaseItemForm(request.POST, instance=purchase_item)
        if form.is_valid():
            form.save()
            return redirect(reverse('purchase:show_purchase'))
