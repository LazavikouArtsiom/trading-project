from datetime import datetime
from celery import shared_task

from trading.trades.models import Trade

from .models import SaleOffer, PurchaseOffer
from .selectors import get_sale_offers, get_suitable_offers
from config.celery import app

def notify_user(sale_offer, purchase_offer):
    pass


@app.task()
def perform_trade(id):
    sale_offer = SaleOffer.objects.get(id=id)
    for suitable_offer in sale_offer.suitable_offers.all():
        if suitable_offer.status == 'opened':
            trade = Trade.objects.create(sale_offer=sale_offer,
                                  purchase_offer=suitable_offer,
                                  status='opened')
            trade.save()

@shared_task
def search_offers():
    print('11')
    sale_offers = get_sale_offers()

    for offer in sale_offers:
        purchase_offers = list(get_suitable_offers(offer.id))

        offer.suitable_offers.add(*purchase_offers)
        offer.save()

        perform_trade.delay(offer.id)
