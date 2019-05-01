from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"home.html",{})

def description(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"description.html",{})

def photos(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"photos.html",{})

def login(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"login.html",{})

def signin(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"signin.html",{})




