from django.urls import path

from purchase import views

app_name = 'purchase'

urlpatterns = [
    path('<int:pk>/', views.add_item_to_cart, name='add_item_to_cart'),
]
