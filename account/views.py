from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from account.models import Account


def login(request):
    return render(request,'account/login.html',{})
    #def post(reques):
    #    request.Post
    #    return render(request,)

def authenticate(request):
    user1 = authenticate(request.POST['username'] ,request.POST['password'])
    if(user1 is None):
        return HttpResponseRedirect(reverse('account:login'))
    account = get_object_or_404(Account,user = user1)
    return HttpResponseRedirect(reverse('account:showProfile', arg=(request.POST['username'],)))
def showProfile(request,username):
    response = "Hell %s."
    return HttpResponse(response % username)