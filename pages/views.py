from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Home Depot Price History!</h1>")
    return render(request, "home.html", {})
def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About Price History!</h1>")