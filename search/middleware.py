import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import django
import os
import sys
sys.path.insert(0, os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "price_comparison_site.settings")
django.setup()
from search import two


class MainCrawler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #q_value = getattr(request, 'q_value', None)
        #two.coupang(q_value)
        
        response = self.get_response(request)
        return response