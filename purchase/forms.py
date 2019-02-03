from django import forms

from .models import PurchaseItem, Purchase


class EditPurchaseItemForm(forms.ModelForm):
    class Meta(object):
        model = PurchaseItem
        fields = ('amount',)
        labels = {'amount': 'مقدار به کیلوگرم'}


class FinalizePurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FinalizePurchaseForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(
            attrs={'rows': 1, 'cols': 40, 'placeholder': kwargs['instance'].user.account.address or ''})

        self.fields['comment'].widget = forms.Textarea(
            attrs={'rows': 5, 'cols': 40})

        self.fields['locationX'].widget = forms.Textarea(
            attrs={'hidden': "true"})
        self.fields['locationY'].widget = forms.Textarea(
            attrs={'hidden': "true"})

    def clean_address(self):
        data = self.cleaned_data['address']
        if not data:
            raise forms.ValidationError("You should add address")
        return data

    class Meta(object):
        model = Purchase
        fields = ('address', 'comment', 'locationX', 'locationY')
        labels = {'address': 'Address', 'comment': 'Comment', 'locationX': '', 'locationY': ''}