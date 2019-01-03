from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='registration'),
    path('login/',
         auth_views.LoginView.as_view(template_name='account/login.html'),
         name='login'),
    path('profile/', views.show_profile, name='show_profile'),
    path('activate/', views.activate, name='activate'),
    path('forget-password/', views.ForgetPassword.as_view(),
         name='forget_password'),
    path('change-password/', views.ChangePassword.as_view(),
         name='change_password')
]
