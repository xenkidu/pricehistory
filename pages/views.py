from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product, Price
# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Depot Price History!</h1>")

    context = {
        'products': Product.objects.all()
    }

    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "title": "About this App Title",
        "description": "This app is built to give more insight and decision making power.",
    }
    return render(request, "about.html", context)
