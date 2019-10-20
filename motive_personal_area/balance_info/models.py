from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    money = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    minutes = models.TimeField(null=True)
    sms = models.IntegerField(null=True)
    traffic = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
