#import pandas as pd
#import numpy as np
import django
#jango.setup()d
from django import forms
from django.db import models
#from sklearn import linear_model
from django.contrib.auth.models import User
from landing.models import Schedule, Subjects, Schedule,Marks

# new_df = pd.read_csv('house.csv', error_bad_lines=False)
# # df1.columns = ['name1']
# # new_df = df1['name1'].str.split(';', expand=True)
# # new_df.to_csv('house.csv')
# # new_df.columns=['0','1','2','3','4','5']
# reg = linear_model.LinearRegression()
# reg.fit(new_df[['0', '1', '5']], new_df['4'])
# # кол-во комнат\ квадратура\ ценовая категория по геолокации\ цена текущая
# # print(reg.coef_)
# # print(reg.intercept_)
# obj = Houses.objects.get(id=1858)
# obj.average_price = reg.predict([[1, 33.5, 2]])
# obj.save()
# print('end')
# us = User.objects.get(id=11)
# us.save()
# hou = Houses.objects.get(user=request.user).favourites.all()
# hou.save()
# hou.favourites.add()

# hu = hou.favourites.all()

# use = User.objects.get(id=1)
# use.save()
#obj1 = Subjects()
#obj1.code_subject = ("1")
#obj1.name = ("Русский")
#obj1.subject_homework_id=("1")
#obj1.subject_marks_id=("1")
#obj1.subject_schedule_id=("1")
#obj1.save()

obj1 = Subjects.objects.get(subject_schedule__day=1)
print(obj1.name)
#obj2 = obj1.favourites.all()
#print(User.objects.get(user=request.user).favorites.all())




