from django.shortcuts import render

from .models import Product, Price

import datetime
# Create your views here.


def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    price = Product.get_product_price(obj)
    context = {
        'title': obj.title,
        'img_url': obj.image_url,
        'price_chart': obj.price_chart,
        'description': obj.description,
        'price': price.price,
    }
    return render(request, 'product/detail.html', context)


def update_prices_view(request):
    objects = Product.objects.all()
    for obj in objects:
        obj.get_product_price()
    return render(request, "home.html", {})


def update_charts_view(request):
    for obj in Product.objects.all():
        obj.make_chart()
    return render(request, "home.html", {})
