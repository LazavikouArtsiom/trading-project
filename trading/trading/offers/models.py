from django.db import models
from django.conf import settings

from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency


STATUSES = (
        ('opened', "opened"),
        ('waiting', "waiting"),
        ('closed', "closed"),
    )


class PurchaseOffer(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=7, choices=STATUSES)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Purchase offer {self.currency} {self.quantity} {self.price}'


class SaleOffer(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    suitable_offers = models.ForeignKey(PurchaseOffer, on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=7, choices=STATUSES)


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Sale offer {self.inventory_item.currency} {self.quantity} {self.price}'



