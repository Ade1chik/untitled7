import pandas as pd
import numpy as np
import django
django.setup()
from django import forms
from sklearn import linear_model
from landing.models import Houses
from django.contrib.auth.models import User

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
obj1 = Houses.objects.get(id=1860)
obj1.save()
obj2 = obj1.favourites.all()
print(User.objects.get(user=request.user).favorites.all())




