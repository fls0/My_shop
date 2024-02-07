from datetime import datetime

from django.db import models
from django.db.models import ImageField


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='catalog', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='products', blank=True)

    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

