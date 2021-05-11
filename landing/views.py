from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .models import Users, Subjects, Schedule, Pass, Teachers, Marks, Subscriber
from django.contrib.auth.models import User
from requests.auth import HTTPBasicAuth
from getpass import getpass
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Schedule, Subjects

# def index(request):
#     obj = Houses.objects.all()
#     context_dict = {'houses': obj}
#     return render(request, 'landing/house.html', context_dict)

def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
    return render(request, 'dilary/services.html', locals())


def home(request):

    return render(request, 'dilary/index.html', locals())


def contacts(request):

    return render(request, 'dilary/contact.html', locals())


# def favourites(request):
#     return render(request, 'landing/favourites.html', locals())

@login_required(login_url='landing')
def house(request):
    obj = Houses.objects.filter(pk__gt=1849)
    # use = User.objects.all()
    # us = request.user
    # use2 = User.objects.get(username=us)
    # use3 = use2.id
    # obj2.favourites.add(use2)
    # use = request.user.is_authenticated
    # if useRS == request.user:
    #     use = useRS
    # if use == request.user:
    #     us = use
    # us = User.objects.filter(user=request.user)
    us = request.user
    use2 = User.objects.get(username=us)
    use3 = use2.id
    use = User.objects.get(id=use3)
    form = HouseForm(request.POST or None)
    print(use)
    h = 1848

    return render(request, 'landing/house.html', locals())


def fav(request, obj1_id):

    us = request.user
    use2 = User.objects.get(username=us)
    use3 = use2.id
    use = User.objects.get(id=use3)

    ob = Houses.objects.get(id=obj1_id)
    ob.favourites.add(use)
    print(ob)
    print(use)
    # form = HouseForm(request.POST or None)
    # if form.is_valid():
    #     obj1 = form.cleaned_data.get("obj1")
    # use = User.objects.all()
    # us = request.user
    # use2 = User.objects.get(username=us)
    # use3 = use2.id
    # obj1.save()
    # use2.save()
    # obj1.favourites.add(use2)
    # print(obj1)
    # print(use2)
    return render(request, 'landing/house.html', locals())


#def loginView(request):
  #  if request.method == "POST":
 ##       form = AuthenticationForm(request.POST)
   #    if form.is_valid():
   #         form.save()
   #         return redirect('login_url')
   # else:
  #      form = AuthenticationForm()

  #  return render(request, 'landing/login.html', {'form': form})


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'landing/register.html', {'form': form})


@login_required(login_url='landing')
def favourites(request):
    
    use = User.objects.all()
    us = request.user
    use2 = User.objects.get(username=us)
    use3 = use2.id
    # ose1 = Houses.objects.all()
    # for user in ose1:
    ose1 = User.objects.get(id=use3)
    ose4 = Houses.objects.get(id=1849)
    ose4.save()
    ose5 = User.objects.get(id=use3).houses_set.all().values()
    print(ose5)

    return render(request, 'landing/favourites.html', locals())


def new(request):

    return render(request, 'dilary/about.html', locals())


def new2(request):

    return render(request, 'dilary/signup.html', locals())


def new3(request):
    use = User.objects.all()
    us = request.user
    use2 = User.objects.get(username=us)
    use3 = use2.id
    ose5 = User.objects.filter(id=use3)
    return render(request, 'dilary/st.html', context={'ose5': ose5 })


def new5(request):
    ose = Subjects.objects.filter(subject_schedule__day=1,).order_by('subject_schedule__lesson_number')
    ose1 = Subjects.objects.filter(subject_schedule__day=2).order_by('subject_schedule__lesson_number')
    ose2 = Subjects.objects.filter(subject_schedule__day=3).order_by('subject_schedule__lesson_number')
    ose3 = Subjects.objects.filter(subject_schedule__day=4).order_by('subject_schedule__lesson_number')
    ose4 = Subjects.objects.filter(subject_schedule__day=5).order_by('subject_schedule__lesson_number')
    ose5 = Subjects.objects.filter(subject_schedule__day=6).order_by('subject_schedule__lesson_number')

    return render(request, 'dilary/res.html', context={'ose': ose, 'ose2': ose2, 'ose3': ose3, 'ose4': ose4,
                                                       'ose5': ose5, 'ose1': ose1 })

def new4(request):

    return render(request, 'dilary/index3.html', locals())



