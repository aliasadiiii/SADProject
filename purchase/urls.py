from django.urls import path

from purchase import views

app_name = 'purchase'

urlpatterns = [
    path('add/<int:product_id>/', views.add_item_to_cart, name='add_item_to_cart'),
    path('', views.show_cart)
]
