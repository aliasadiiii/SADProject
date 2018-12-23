from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from account.forms import SignupForm
from account.models import Account


def show_profile(request, username):
    response = "Hell %s."
    return HttpResponse(response % username)


class Register(View):
    @staticmethod
    def get(request):
        form = SignupForm()
        return render(request, 'account/register.html', {'form':form})

    @staticmethod
    def post(request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            user = User(username = username, password = password)
            user.save()
            account = Account(user=user,phone=phone)
            account.save()
            return HttpResponse("Registration completed.")
        return render(request, 'account/register.html', {'form': form})
