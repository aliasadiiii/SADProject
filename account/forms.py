from django.contrib.auth.forms import UserCreationForm
from django import forms

def phoneValidator(phone):
    return len(phone) == 11 and str(phone).isalnum()

class SignupForm(UserCreationForm):
    phone = forms.CharField(validators=[phoneValidator,])
