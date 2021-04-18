# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled1.settings")
import pandas as pd
import numpy as np
import django
django.setup()
from django import forms
from sklearn import linear_model
from django.db import migrations, models
from django.urls import path
from landing.models import Houses
from django.conf import settings


URL = 'https://www.avito.ru/kazan/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.197 Yowser/2.5 Yptp/1.23 Safari/537.36', 'accept':'*/*'}
HOST = 'https://www.avito.ru'
FILE = 'house1.csv'


def get_html(url, params=None):
    r = requests.get(url,  params=params, headers=HEADERS)
    return r


# def get_pages_count(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     pagination = soup.select('span', class_='snippet-horizontal   item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended')
#     if pagination:
#         return int(pagination[0].get_text())
#     else:
#         return 1


def get_content(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='item_table-wrapper')
        house = []
        for item in items:
            house.append({
                'title': item.find('div', class_='snippet-title-row').get_text(strip=True).replace('-к квартира', '').replace('Студия', '0.5').replace('м²', '').replace('Онлайн-показ', '').replace('эт.', '').replace(',', ';').replace('Своб. планировка', '0'),
                'link': HOST+item.find('a', class_='snippet-link').get('href'),
                'usd_prise': item.find('div', class_='snippet-price-row').get_text().replace('\n', '').replace('₽', '').replace(' ', ''),
                'geo1': item.find('div', class_='item-address-georeferences').get_text().replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('км', '').replace(' ', '').replace(',', '').replace('00 м', '').replace('р-нНово-Савиновский', '3').replace('Аметьево', '3').replace('р-нПриволжский', '2').replace('Горки', '2').replace('ПроспектПобеды', '2').replace('ПлощадьТукая', '3').replace('р-нСоветский', '2').replace('Северныйвокзал', '1').replace('Яшьлек', '2').replace('КозьяСлобода', '3').replace('Дубравная', '2').replace('р-нКировский', '1').replace('р-нМосковский', '1').replace('Суконнаяслобода', '3').replace('Авиастроительная', '1').replace('Кремлёвская', '4').replace('р-нАвиастроительный', '1'),
                #'image': item.find('div',class_='item-slider-image').get_image()
            })
        return house
    except AttributeError:
        print(1)


def get_content1(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='item__line')
        house = []
        for item in items:
            house.append({
                'title': item.find('div', class_='snippet-title-row').get_text(strip=True),
                'link': HOST + item.find('a', class_='snippet-link').get('href'),
                'usd_prise': item.find('div', class_='snippet-price-row').get_text().replace('\n', '').replace('₽', '').replace(' ', ''),
                'geo1': item.find('div', class_='item-address-georeferences').get_text(),
                'image': item.find('img').get('src')
            })
        return house
    except AttributeError:
        print("error")


def save_file(items, path):
    with open(path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        #writer.writerow(['df'])
        for item in items:
            item['title'] = item['title'].split('/', 1)[0]
            if item['geo1'] == '':
                item['geo1'] = '2'
            writer.writerow([item['title'], item['link'], item['usd_prise'], item['geo1']])


def save_bd(items):
    try:
        for item in items:
            print(item['image'])
            obj = Houses()
            obj.har = (item['title'])
            obj.http = (item['link'])
            obj.price = (item['usd_prise'])
            obj.image = str(item['image'])
            obj.geo = (item['geo1'])
            obj.save()
    except TypeError:
        print("error")


def save_db():
    html = get_html(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup.find_all('div', class_='item__line'))
    if html.status_code == 200:
        house = []
        # pages_count = get_pages_count(html.text)
        for page in range(1, 10):
            print(f'запись в бд {page} из {"x"}...')
            html = get_html(URL, params={'page': page})
            house.extend(get_content1(html.text))
            print(house)
            save_bd(house)
        print(len(house))
    else:
        print('Error')


def parse():
    #URL = input('Введите URL: ')
    #URL = URL.strip()
    html = get_html(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup.find_all('div', class_='item_table-wrapper'))
    if html.status_code == 200:
        house = []
        list1 = []
        # pages_count = get_pages_count(html.text)
        for page in range(1, 30):
            print(f'парсинг странницы {page} из {30}...')
            html = get_html(URL, params={'page': page})
            #list1.append(get_content(html.text))
            house.extend(get_content(html.text))
            print(house)
        save_file(house, FILE)
        print(len(house))
        os.startfile(FILE)
    else:
        print('Error')


# obj = Houses.objects.get(id=1007)
# obj.image = ('https://60.img.avito.st/640x480/4941878960.jpg')
# obj.geo = ('Республика Татарстан, Казань, улица Гарифа Ахунова, 18')
# obj.save()

parse()
# save_db()

# df1 = pd.read_csv('house1.csv', error_bad_lines=False)
# df1.columns = ['name1']
# new_df = df1['name1'].str.split(';',expand=True)
# new_df.to_csv('house.csv')
# new_df.columns=['0','1','2','3','4','5']
# reg = linear_model.LinearRegression()
# reg.fit(new_df[['0', '1', '5']], new_df['4'])
# print(reg.coef_)
# print(reg.intercept_)
# print(reg.predict([[1, 36,  1]]))

# tom = Houses.objects.get(id=1)
# tom.delete()
# tom.har = 'testHouse'
# tom.http = 'http:/adel/first'
# tom.price = 25000000
# tom.save()