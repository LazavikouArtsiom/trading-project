from django.db import transaction

from .services import (calculate_transaction_quantity,
                       calcuclate_money,
                       close_offers,
                       offers_trade,
                       )


def perform_trade_presave(sender, instance, **kwargs):
    from .models import Trade

    sale_offer = instance.sale_offer
    purchase_offer = instance.purchase_offer
    
    sale_quantity_before_trade = sale_offer.quantity
    purchase_quantity_before_trade = purchase_offer.quantity
           
    with transaction.atomic():
        offers_trade(sale_offer, purchase_offer)

    sale_quantity_after_trade = sale_offer.quantity
    purchase_quantity_after_trade = purchase_offer.quantity

    instance.purchase_quantity_before_trade = purchase_quantity_before_trade
    instance.purchase_quantity_after_trade = purchase_quantity_after_trade
    instance.sale_quantity_before_trade = sale_quantity_before_trade
    instance.sale_quantity_after_trade = sale_quantity_after_trade

