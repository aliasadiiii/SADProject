from django.urls import path

from account import views


app_name = 'account'
urlpatterns = [
    path('', views.login, name = 'login'),
    path('authenticate/',views.authenticate, name = 'authenticate'),
    path('profile/',views.showProfile,name = 'showProfile')
]