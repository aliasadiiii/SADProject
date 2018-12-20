from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse

from account.models import Account


def login(request):
    print('1')
    return render(request, 'account/login.html',{})
    #def post(reques):
    #    request.Post
    #    return render(request,)


def authentication(request):
    print('2')
    user1 = authenticate(username = request.POST['username'], password = request.POST['pass'])
    if(user1 is None):
        return HttpResponseRedirect(reverse('account:login'))
    account = get_object_or_404(Account,user = user1)
    return HttpResponseRedirect(reverse('account:showProfile', args=(request.POST['username'], )))


def showProfile(request, username):
    response = "Hell %s."
    return HttpResponse(response % username)