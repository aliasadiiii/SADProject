from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.models import Account, phone_validator


class SignupForm(UserCreationForm):
    phone = forms.CharField(validators=[phone_validator])
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
    class Meta:
        model = Account
        fields = ["name", "phone", "avatar"]
        labels = {"name": "نام", "phone": "شماره تماس", "avatar": "نمایه"}

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field in ["name", "phone"]:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        for field in ["avatar"]:
            self.fields[field].widget.attrs.update(
                {"class": "form-control-file"})
