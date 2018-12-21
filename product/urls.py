from django.urls import path
from product import views

urlpatterns = [
    path('list', views.product_list, name='product_list')
]
