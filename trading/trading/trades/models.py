from django.db import models
from django.db.models.signals import pre_save

from trading.offers.models import SaleOffer, PurchaseOffer
from trading.trades.signals import perform_trade_presave


class Trade(models.Model):

    STATUSES = (
        ('opened', "opened"),
        ('closed', "closed"),
    )

    sale_offer = models.ForeignKey(SaleOffer, on_delete=models.CASCADE)
    purchase_offer = models.ForeignKey(PurchaseOffer, on_delete=models.CASCADE)

    purchase_quantity_before_trade = models.PositiveIntegerField(blank=True, null=True, default=0)
    purchase_quantity_after_trade = models.PositiveIntegerField(blank=True, null=True, default=0)
    sale_quantity_before_trade = models.PositiveIntegerField(blank=True, null=True, default=0)
    sale_quantity_after_trade = models.PositiveIntegerField(blank=True, null=True, default=0)
    status = models.CharField(max_length=6, choices=STATUSES, default='opened')

    def __str__(self):
        return f'STATUS {self.status} {self.sale_offer} {self.purchase_offer}'

    class Meta:
        unique_together = ['sale_offer', 'purchase_offer']

pre_save.connect(perform_trade_presave, sender=Trade)