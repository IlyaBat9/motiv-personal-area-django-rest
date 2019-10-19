from django.contrib.auth.models import User
from django.db import models


class Tariff(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    description = models.CharField(max_length=2048)
    minutes = models.IntegerField()
    sms = models.IntegerField()
    traffic = models.IntegerField(default=0)
