from datetime import datetime

from celery import shared_task
from django.db import transaction

from trading.trades.models import Trade
from .models import SaleOffer, PurchaseOffer
from .selectors import get_sale_offers
from .services import add_suitable_offers_into_field
from config.celery import app


@app.task()
def perform_trade(id):
    sale_offer = SaleOffer.objects.get(id=id)
    for suitable_offer in sale_offer.suitable_offers.all():
        with transaction.atomic():
            if suitable_offer.status == 'opened' and sale_offer.quantity:
                trade = Trade.objects.create(sale_offer=sale_offer,
                                             purchase_offer=suitable_offer,
                                             status='opened')
                trade.save()


@shared_task
def search_offers():
    sale_offers = get_sale_offers()

    for offer in sale_offers:
        add_suitable_offers_into_field(offer)

        perform_trade.delay(offer.id)
    