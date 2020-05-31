from django.shortcuts import render
from django.http import HttpResponse

from . import templates

def index(request):
    context = {
        "name" : "Sergey Gusev",
        "signin" : "/signin",
        "style" : "css/css.css"
    }
    return render(request, 'mytestproj/templates/index.html', context)

def signin(request):
    if request.method == 'GET':
        context = {
            "signin" : "/signin",
            "signup" : "/signup",
            "style" : "css/css.css"
        }
        return render(request, 'mytestproj/templates/form/signin.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        # Check in DataBase
        context = {
            "username" : username,
            "style" : "css/css.css"
        }
        return render(request, 'mytestproj/templates/index.html', context)

def signup(request):
    if request.method == 'GET':
        context = {
            "signup" : "/signup",
            "style" : "css/css2.css"
        }
        return render(request, 'mytestproj/templates/form/signup.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        # Check in DataBase
        context = {
            "username" : username,
            "style" : "css/css.css"
        }
        return render(request, 'mytestproj/templates/index.html', context)
