from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120,)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    homedepot_url = models.CharField(max_length=240,)
    image_url = models.CharField(max_length=240,)
    price_chart = models.CharField(max_length=120,)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title