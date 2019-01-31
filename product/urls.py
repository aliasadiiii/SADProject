from django.urls import path, re_path
from product import views

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_page, name='product_page'),
    path('<int:product_id>/post_comment/', views.add_comment_to_product, name='add_comment_to_product'),
]
