from django.urls import path, include
from .views import about_us, home

urlpatterns = [
    path('about-us/', about_us, name='about-us'),
    path('', home, name='home')
]