from django.urls import path

from account import views


app_name = 'account'
urlpatterns = [
    path('', views.login, name = 'login'),
    path('authenticate/',views.authentication, name = 'authentication'),
    path('profile/',views.showProfile,name = 'showProfile')
]