from django.urls import path

from purchase import views

app_name = 'purchase'

urlpatterns = [
    path('edit/<int:purchase_item_id>/', views.EditPurchaseItemView.as_view(), name='edit_purchase_item'),
    path('delete/<int:purchase_item_id>/', views.delete_purchase_item, name='delete_purchase_item'),
    path('add/<int:product_id>/', views.add_item_to_purchase, name='add_item_to_purchase'),
    path('', views.show_purchase, name='show_purchase')
]
