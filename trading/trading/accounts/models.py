from django.conf import settings
from django.db import models


class Account(models.Model):

    money = models.PositiveIntegerField(default=0)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'acount {self.user.username} {self.money}'

    def add_money(self, money):
        self.money += money
        self.save()

    def remove_money(self, money):
        self.money -= money
        self.save()
