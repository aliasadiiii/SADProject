from django.urls import path

from purchase import views

app_name = 'purchase'

urlpatterns = [
    path('finalize_purchase/', views.FinalizePurchaseView.as_view(), name='finalize_purchase'),
    path('edit/<int:purchase_item_id>/', views.EditPurchaseItemView.as_view(), name='edit_purchase_item'),
    path('delete/<int:purchase_item_id>/', views.delete_purchase_item, name='delete_purchase_item'),
    path('add/<int:product_id>/', views.add_item_to_purchase, name='add_item_to_purchase'),
    path('history', views.show_history, name='show_history'),
    path('purchase_details/<str:reference_token>/', views.purchase_details, name='purchase_details'),
    path('', views.show_purchase, name='show_purchase')
]
