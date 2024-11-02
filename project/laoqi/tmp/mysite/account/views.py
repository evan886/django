from django.shortcuts import render
from django.http  import  HttpResponse, HttpResponseRedirect
from django.contrib.auth import  authenticate,login
from .forms import LoginForm #, RegistrationForm, UserProfileForm, UserForm, UserProfileForm, UserInfoForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User
from django.urls import reverse

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user =  authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("Weclome you.  auth successfully")
            else:
                return HttpResponse("Wellcome username or password is not right.")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})



# Create your views here.
