from django.db import models


class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    homedepot_url = models.TextField()
    image_url = models.TextField()
    price_chart = models.TextField()

    def __str__(self):
        return self.title