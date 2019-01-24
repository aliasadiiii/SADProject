from django import forms

from .models import PurchaseItem


class EditPurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ('amount',)
        labels = {'amount': 'مقدار به کیلوگرم'}
