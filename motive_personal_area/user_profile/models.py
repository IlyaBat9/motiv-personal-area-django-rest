from django.contrib.auth.models import User
from django.db import models

from balance_info.models import Balance


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    balance = models.OneToOneField(Balance, on_delete=models.CASCADE, default=None)

    def get_full_name(self):
        if self.middle_name in None:
            return "{0} {1}".format(self.first_name, self.last_name)
        return "{0} {1} {2}".format(self.first_name, self.middle_name, self.last_name)

