from django.shortcuts import render

from .models import Product
# Create your views here.


def product_detail_view(request):
    obj = Product.objects.get(id=4)
    context = {
        'title': obj.title,
        'img_url': obj.image_url,
        'description': obj.description,
    }
    return render(request, 'product/detail.html', context)
