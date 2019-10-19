from django.db import models


class Balance(models.Model):
    money = models.IntegerField(default=0)
    minutes = models.IntegerField(null=True)
    sms = models.IntegerField(null=True)
    traffic = models.IntegerField(null=True)
