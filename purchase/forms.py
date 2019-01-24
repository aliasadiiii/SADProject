from django import forms

from account.models import Address

from .models import PurchaseItem, Purchase


class EditPurchaseItemForm(forms.ModelForm):
    class Meta(object):
        model = PurchaseItem
        fields = ('amount',)
        labels = {'amount': 'مقدار به کیلوگرم'}


class FinalizePurchaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FinalizePurchaseForm, self).__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.filter(
            user=kwargs['instance'].user)

        self.fields['comment'].widget = forms.Textarea(
            attrs={'rows': 5, 'cols': 41})

    def clean_address(self):
        data = self.cleaned_data['address']
        if data is None:
            raise forms.ValidationError("You should add address")
        return data

    class Meta(object):
        model = Purchase
        fields = ('address', 'comment')
