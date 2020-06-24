from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120,)
    description = models.TextField(blank=True)
    homedepot_url = models.CharField(max_length=240,)
    image_url = models.CharField(max_length=240,)
    price_chart = models.CharField(max_length=120,)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField(auto_now=True)