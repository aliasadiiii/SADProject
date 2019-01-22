from django.contrib.auth import views as auth_views
from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.Register.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/', views.show_profile, name ='profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),

    path('activate/', views.activate, name='activate'),
    path('forget_password/', views.ForgetPassword.as_view(), name='forget_password'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
]
