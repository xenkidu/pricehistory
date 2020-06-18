from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Depot Price History!</h1>")
    context = {
        "title": "Home Page Title",
        "description": "This app is built to give more insight and decision making power.",
        "products": ['Ryobi Drill', 'Dewalt Drill', 'Saw', 'Hammer Drill']
    }
    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    context = {
        "title": "About this App Title",
        "description": "This app is built to give more insight and decision making power.",
    }
    return render(request, "about.html", context)
