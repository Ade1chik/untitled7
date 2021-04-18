"""untitled1 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/', views.landing, name='landing'),
    url(r'^favourites/', views.favourites, name='favourites'),
    url(r'^login/',  views.LoginView.as_view(template_name='landing/login.html'), name='login_url'),
    url(r'^logout/',  auth_views.LogoutView.as_view(template_name='landing/logout.html'), name='logout_url'),
    url(r'^register/', views.registerView, name="register_url"),
    url(r'^house/', views.house, name='house'),
    path("<obj1_id>/house/", views.fav, name="fav"),
    url(r'^favourites/', views.favourites, name='favourites'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^new/', views.new, name='new'),
    url(r'^new2/', views.LoginView.as_view(template_name='dilary/signup.html'), name='new2'),
    url(r'^new3/', views.new3, name='new3'),
    url(r'^new5/', views.new5, name='new5'),
    url(r'^new4/', views.new4, name='new4')
]
