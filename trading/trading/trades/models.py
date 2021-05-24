from django.db import models
from trading.offers.models import SaleOffer, PurchaseOffer

class Trade(models.Model):

    STATUSES = (
        ('opened', "opened"),
        ('closed', "closed"),
    )

    sale_offer = models.ForeignKey(SaleOffer, on_delete=models.CASCADE)
    purchase_offer = models.ForeignKey(PurchaseOffer, on_delete=models.CASCADE)

    status = models.CharField(max_length=6, choices=STATUSES)

    def __str__(self):
        return f'STATUS {self.status} {self.sale_offer.id} {self.purchase_offer.id}'