from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="Friends Index" ),
    path("register/", views.register, name="register")
]