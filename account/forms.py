from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import Account


def phone_validator(phone):
    return len(phone) == 11 and str(phone).isalnum()


class SignupForm(UserCreationForm):
    phone = forms.CharField(validators=[phone_validator, ])
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User exists with email")
        return email


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                label="Password Confirmation")

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password2', "Passwords don't match.")

class EditProfileForm(forms.ModelForm):
    model = Account
