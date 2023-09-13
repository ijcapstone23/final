import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium
import re
import requests
import django
import os
import sys
sys.path.insert(0, os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "price_comparison_site.settings")
django.setup()
import pandas as pd

def coupang(query):
    driver = webdriver.Chrome()
    from search.models import Product
    from django.contrib import admin

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    def url(i):
        return "https://www.coupang.com/np/search?q="+query+"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str()+"&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    def noNone(value):
        return '' if value is None else value

    for y in range(1,10):
        res = requests.get(url(y), headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "lxml")

        items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
        for item in items:

            name = item.find("div", attrs={"class": "name"})
            if name:
                name = name.get_text()
            else:
                name = ''

            price = item.find("strong", attrs={"class": "price-value"})
            if price:
                price = price.get_text()
            else:
                price = '0'
            price_int = int(price.replace(',', ''))

            rate = item.find("em", attrs={"class": "rating"})
            if rate:
                rate = rate.get_text()
            else:
                rate = 0

            purl = item.find("a", attrs={"class": "search-product-link"}).get('href')

            image = '//dummyimage.com/200x200/5558a4/fff.gif&text=No+Image'

            item = Product(product_name=noNone(name), shop_name='쿠팡', price=price_int,
                        detail='', imgurl='https:' + noNone(image), url='https://www.coupang.com/' + noNone(purl), star=noNone(rate))
            item.save()

        time.sleep(0.5)
    return "Done!"
