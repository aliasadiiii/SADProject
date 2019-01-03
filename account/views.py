from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View

from account.forms import ChangePasswordForm, ForgetPasswordForm, SignupForm
from account.models import Account
from account.utils import send_activation_email, send_forget_password_email


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
            account.activation_token = account.generate_random_token()
            account.save()

            activation_link = "{}{}?token={}".format(
                settings.HOST_NAME,
                reverse('activate'),
                account.activation_token)
            send_activation_email(to=email, activation_link=activation_link)

            return redirect(reverse('home'))
        return render(request, 'account/register.html', {'form': form})


def activate(request):
    token = request.GET.get('token')
    try:
        account = Account.objects.get(activation_token=token)
        account.user.is_active = True
        account.user.save()
        return redirect(reverse('home'))
    except Account.DoesNotExist:
        return HttpResponse("کاربر موردنظر وجود نداشت", status=404)


class ForgetPassword(View):
    @staticmethod
    def get(request):
        form = ForgetPasswordForm()
        return render(request, 'account/forget_password.html', {'form': form})

    @staticmethod
    def post(request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                account = Account.objects.get(user__email=email)
                account.forget_password_token = account.generate_random_token()
                account.save()
                forget_password_link = "{}{}?token={}".format(
                    settings.HOST_NAME,
                    reverse('change_password'),
                    account.forget_password_token)

                send_forget_password_email(
                    email,
                    forget_password_link=forget_password_link
                )
                return redirect(reverse('home'))
            except Account.DoesNotExist:
                return render(request, 'account/forget_password.html',
                              {'form': form})

        return render(request, 'account/forget_password.html',
                      {'form': form})


class ChangePassword(View):
    @staticmethod
    def get(request):
        token = request.GET.get('token')
        try:
            Account.objects.get(forget_password_token=token)
            form = ChangePasswordForm()
            return render(request, 'account/change_password.html',
                          {'form': form})
        except Account.DoesNotExist:
            return HttpResponse("کاربر موردنظر وجود نداشت", status=404)

    @staticmethod
    def post(request):
        token = request.GET.get('token')
        try:
            account = Account.objects.get(forget_password_token=token)
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password1']
                account.user.set_password(password)
                account.user.save()
                return redirect(reverse('home'))
            return render(request, 'account/change_password.html',
                          {'form': form})
        except Account.DoesNotExist:
            return HttpResponse("کاربر موردنظر وجود نداشت", status=404)
