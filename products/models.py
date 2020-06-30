from django.db import models

import datetime
import time
import requests
from bs4 import BeautifulSoup
import random

class Product(models.Model):
    title = models.CharField(max_length=120,)
    description = models.TextField(blank=True)
    homedepot_url = models.CharField(max_length=240,)
    image_url = models.CharField(max_length=240,)
    price_chart = models.CharField(max_length=120,)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def add_product(self):
        pass

    def repeat_every_day_at(self, hour=7, minutes=0, seconds=0):
        def dec_repeat(fn):
            def wrapper(*args, **kwargs):
                today = datetime.datetime.today()
                tomorrow = today.replace(day=today.day, hour=hour, minute=minutes, second=seconds)
                while True:
                    # update today
                    today = datetime.datetime.today()
                    if today < tomorrow:
                        # sleep while true
                        time.sleep(3600)
                    else:
                        # call the function
                        fn(*args, **kwargs)
                        # update today so this continue forever
                        tomorrow = tomorrow.replace(day=tomorrow.day + 1, hour=hour, minute=minutes, second=seconds)
            return wrapper
        return dec_repeat

    def set_header_info(self):
        # set information before performing a request, otherwise access to homedepot is blocked.
        location = "Denver, Colorado"
        params = {'address': location}
        referer = "https://www.google.com/"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36',
            'referer': referer,
            'upgrade-insecure-requests': '1',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1'
        }
        return params, referer, headers

    def get_product_price(self):
        price = self.price_set.filter(date=datetime.date.today())
        if price:
            return price[0]
        # set header info
        params, referer, headers = self.set_header_info()
        # perform a random sleep
        # time.sleep(random.random() * 1)
        # perform a request and fetch data with soup
        r = requests.get(url=self.homedepot_url, params=params, headers=headers)
        soup = BeautifulSoup(r.content, features="html.parser")
        # get price and strip whitespace
        price = soup.find('span', attrs={'class': 'price__dollars'}).text.strip().replace(',', '')
        cents = soup.find('span', attrs={'class': 'price__cents'}).text.strip()
        print('price:', price)
        print('cents:', cents)
        if not price:
            price = -1
        else:
            price = float(price + '.' + cents)
        return self.price_set.create(price=price)


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"product_id: {self.product.id}, price: {self.price}"