import csv
from rangefilter import filter

from django.contrib import admin
from django.http import HttpResponse

from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_filter = (('date', filter.DateRangeFilter), 'state')
    actions = ['export_as_csv']

    def export_as_csv(self, _request, queryset):
        field_names = ['reference_token', 'date', 'state', 'address', 'comment',
                       'products', 'price']

        response = HttpResponse(content_type='text/csv', charset='utf-8')
        response['Content-Disposition'] = 'attachment; filename=purchase.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            products = ', '.join(
                obj.purchaseitem_set.values_list('product__name', flat=True))
            price = 0
            for p in obj.purchaseitem_set.all():
                price += p.fee * p.amount
            writer.writerow(
                [obj.reference_token, obj.date, obj.state, obj.address,
                 obj.comment, products, price])

        return response

    export_as_csv.short_description = "Export Selected"
