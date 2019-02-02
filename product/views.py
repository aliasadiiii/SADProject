from datetime import date

import jdatetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, get_object_or_404, redirect

from account.models import Account
from product.forms import CommentForm
from .models import Product, Comment


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
    p = Product.objects.get(id=product_id)
    product = {'name': p.name,
               'price': p.price,
               'is_available': p.is_available,
               'expires_at': jdatetime.date.fromgregorian(date=p.expires_at),
               'manufacture_date': jdatetime.date.fromgregorian(
                   date=p.manufacture_date),
               'photo': p.photo,
               'product_id': p.id}
    comments = Comment.objects.filter(product=p, approved=True)
    form = CommentForm()

    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
    else:
        account = None

    return render(request, 'product_page.html',
                  context={'product': product, 'comments': comments, 'form':form,
                           'account': account})


@login_required
def add_comment_to_product(request, product_id):
    p = get_object_or_404(Product, id=product_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = p
        u = User.objects.get(username=request.user)
        comment.author = Account.objects.get(user=u)
        comment.save()
        return redirect('product_page', product_id=product_id)
