from datetime import datetime
from django.db import models
from django.conf import settings

from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency


STATUSES = (
    ('opened', "opened"),
    ('closed', "closed"),
)


class Offer:

    def remove_quantity(self, quantity):
        self.quantity -= quantity
        self.save()

    def set_status(self, status):
        self.status = status
        self.save()


class PurchaseOffer(models.Model, Offer):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=7, choices=STATUSES, default='opened')
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Purchase offer {self.user} {self.currency} {self.quantity} {self.price}'


class SaleOffer(models.Model, Offer):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    suitable_offers = models.ManyToManyField(PurchaseOffer, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=7, choices=STATUSES, default='opened')
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Sale offer {self.user} {self.inventory_item.currency} {self.quantity} {self.price}'
