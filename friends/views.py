from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from . import models as forms

# Create your views here.
def index(request):
    return HttpResponse("<h1>Frinds Index</h1>")


def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # form = UserCreationForm()
        form = forms.RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "friends/templates/register.html", context)
