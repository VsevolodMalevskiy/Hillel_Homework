# Описание принципа парсинга https://www.youtube.com/watch?v=0ws5tsRBgL8

import requests
from bs4 import BeautifulSoup
import re
import time
import collections
import copy
import datetime


def url():

    url = 'https://intertop.ua/ua/catalog/muzhskaya_obuv/brand-COLINS_adidas_armani-exchange_bugatti_calvin-' \
          'klein_calvin-klein-jeans_caterpillar_columbia_ecco_filodoro_jack-wolfskin_kappa_merrell_nike_puma_reebok_' \
          'skechers_termit_timberland_wrangler-minimum_price-500_1100-size-41_41-5_42_42-5/'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')

    search_https = list(soup.findAll("div", class_="product-name"))
    search_price = list(soup.findAll("div", class_="product-price"))
    return search_https, search_price


def list_adress(list_https, list_price):
    search_adress = []
    for item in list_https:
        f = re.findall(r"https://intertop.ua/ua/product/+\D*\d*", str(item))
        search_adress.append(f[0])
    # print(seach_adress)
    search_price = []
    for item in list_price:
        f = re.findall(r"[0-9]{3,4}", str(item))
        search_price.append(f[0])
    print(search_price)

    print(len(search_adress))
    print(len(search_price))

    search_exit = []
    for key in range(len(search_adress)):
        search_exit.append(search_adress[key])
        search_exit.append(search_price[key])

    return search_exit


# основное тело
https_temp1, price_temp1 = url()
list_1 = list_adress(https_temp1, price_temp1)

while True:
    time.sleep(180)
    https_temp2, price_temp2 = url()
    list_2 = list_adress(https_temp2, price_temp2)

    if collections.Counter(list_1) == collections.Counter(list_2):
        print(datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H.%M.%S'))
        print("Обновлений нет!")
        list_1 = copy.deepcopy(list_2)
    else:
        print(datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H.%M.%S'))
        print("Есть обновления!!!")
        print(set(list_1).difference(set(list_2)))
        print(set(list_2).difference(set(list_1)))
        list_1 = copy.deepcopy(list_2)


# pyinstaller -F D:\MyPython\Hillel_Homework\Homework\parsing_intertop.py



