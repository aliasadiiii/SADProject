from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View

from account.forms import SignupForm
from account.models import Account


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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            user = User(username=username)
            user.set_password(password)
            user.save()

            account = Account(user=user, phone=phone)
            account.save()
            return redirect(reverse('home'))
        return render(request, 'account/register.html', {'form': form})
