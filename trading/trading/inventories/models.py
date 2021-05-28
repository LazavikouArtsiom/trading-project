
from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404

from trading.items.models import Currency


class InventoryItem(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
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

    def add_item_quantity(self, currency, quantity, user):
        item = InventoryItem.objects.get_or_create(currency=currency, user=user)[0]
        item.quantity += quantity
        item.save()

    def remove_item_quantity(self, currency, quantity, user):
        item = InventoryItem.objects.get(currency__code=currency, user=user)
        item.quantity -= quantity
        item.save()