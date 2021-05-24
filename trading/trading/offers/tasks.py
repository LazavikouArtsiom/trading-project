from datetime import datetime
from celery import shared_task

from trading.trades.models import Trade

from .models import SaleOffer, PurchaseOffer
from .selectors import get_sale_offers, get_suitable_offers


def notify_user(sale_offer, purchase_offer):
    pass


def perform_trade(sale_offer):
    for suitable_offer in sale_offer.suitable_offers.all():
        if suitable_offer.status == 'opened':
            trade = Trade.objects.create(sale_offer=sale_offer,
                                  purchase_offer=suitable_offer,
                                  status='opened')
            trade.save()


def search_offers():
    sale_offers = get_sale_offers()

    for offer in sale_offers:
        purchase_offers = list(get_suitable_offers(offer))

        offer.suitable_offers.add(*purchase_offers)
        offer.save()

        perform_trade(offer)
