from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def add_item_to_cart(request,pk):
    print(request.POST.get('amount'))

    if 'cart' not in request.session:
        request.session['cart'] = {}
    request.session['cart'][pk] = request.POST.get('amount')
    print('cart =', request.session['cart'])

    return HttpResponse("amme")