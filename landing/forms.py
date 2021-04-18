from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]

# class HouseForm(forms.ModelForm):
#
#     class Meta:
#         model = Houses
#         exclude = [""]
class HomeworkForm(forms.ModelForm):

    class Meta:
         model = Homework
         exclude = [""]