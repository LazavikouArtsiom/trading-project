from django.db import models
from django.conf import settings
from django.utils import tree

from trading.items.models import Currency


class Watchlist(models.Model):
    currencies = models.ManyToManyField(Currency,
                                    related_name='currency',
                                    blank=True,
                                    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'watchlist {self.user.username}'
