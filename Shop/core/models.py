from datetime import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(default=datetime.now(), blank=True)


