from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# AbstractUser._meta.get_field('email')._unique = True
# AbstractUser._meta.get_field('email').blank = False

# class User(AbstractUser):
#     pass

# class Article(models.Model):
#     art_id          = models.IntegerField(primary_key=True)
#     title           = models.CharField()
#     description     = models.CharField()
#     author          = models.ForeignKey(User, on_delete=models.CASCADE)
#     publishing_date = models.DateField()

class RegisterForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

