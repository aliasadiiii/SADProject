from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(request, 'general/about_us.html', {})


def home(request):
    return render(request, 'general/home.html')
