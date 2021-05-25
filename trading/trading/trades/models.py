from django.db import models
from django.db.models.signals import pre_save

from trading.offers.models import SaleOffer, PurchaseOffer
from .signals import perform_trade_presave


class Trade(models.Model):

    STATUSES = (
        ('opened', "opened"),
        ('closed', "closed"),
    )

    sale_offer = models.ForeignKey(SaleOffer, on_delete=models.CASCADE)
    purchase_offer = models.ForeignKey(PurchaseOffer, on_delete=models.CASCADE)

    purchase_quantity_before_trade = models.PositiveIntegerField(blank=True, null=True)
    purchase_quantity_after_trade = models.PositiveIntegerField(blank=True, null=True)
    sale_quantity_before_trade = models.PositiveIntegerField(blank=True, null=True)
    sale_quantity_after_trade = models.PositiveIntegerField(blank=True, null=True)

    status = models.CharField(max_length=6, choices=STATUSES)

    def __str__(self):
        return f'STATUS {self.status} {self.sale_offer.id} {self.purchase_offer.id}'

pre_save.connect(perform_trade_presave, sender=Trade)
