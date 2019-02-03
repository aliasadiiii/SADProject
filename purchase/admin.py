import csv
from rangefilter import filter

from django.contrib import admin
from django.http import HttpResponse
# from django_google_maps import fields as map_fields
# from django_google_maps import widgets as map_widgets

from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_filter = (('date', filter.DateRangeFilter), 'state')
    actions = ['export_as_csv']

    def export_as_csv(self, _request, queryset):
        field_names = ['reference_token', 'date', 'state', 'comment']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=purchase.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow(
                [getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
    # formfield_overrides = {
    #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    # }