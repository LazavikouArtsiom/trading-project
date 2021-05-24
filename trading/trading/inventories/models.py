from django.db import models
from django.conf import settings

from trading.items.models import Currency


class InventoryItem(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'inventory item {self.user.username} {self.currency.code} {self.quantity}'


class Inventory(models.Model):
    inventory_items = models.ManyToManyField(InventoryItem, blank=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'inventory {self.user.username}'