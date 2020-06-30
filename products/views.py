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
        'description': obj.description,
        'price': price.price,
    }
    return render(request, 'product/detail.html', context)
