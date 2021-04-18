from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from landing.models import Houses


def index(request):
    obj = Houses.objects.all()
    return render(request, 'landing/house.html', locals())

