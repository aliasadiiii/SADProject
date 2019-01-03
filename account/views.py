from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View

from account.forms import SignupForm
from account.models import Account
from account.utils import send_activation_email


def show_profile(request):
    response = "Hello %s."
    return HttpResponse(response)


class Register(View):
    @staticmethod
    def get(request):
        form = SignupForm()
        return render(request, 'account/register.html', {'form': form})

    @staticmethod
    def post(request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data.get('email')
            user.email = email
            user.is_active = False
            user.save()

            phone = form.cleaned_data.get('phone')
            account = Account.objects.create(user=user, phone=phone)
            account.token = account.generate_random_token()
            account.save()

            activation_link = "{}{}?token={}".format(
                settings.HOST_NAME,
                reverse('activate'),
                account.token)
            send_activation_email(to=email, activation_link=activation_link)

            return redirect(reverse('home'))
        return render(request, 'account/register.html', {'form': form})


def activate(request):
    token = request.GET.get('token')
    try:
        account = Account.objects.get(token=token)
        account.user.is_active = True
        account.user.save()
        return redirect(reverse('home'))
    except Account.DoesNotExist:
        return HttpResponse("کاربر موردنظر وجود نداشت", status=404)
