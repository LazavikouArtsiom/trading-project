from django.db import transaction

from trading.trades import services


def perform_trade_presave(sender, instance, **kwargs):
    
    from .models import Trade

    if not instance.status == 'closed':

        sale_offer = instance.sale_offer
        purchase_offer = instance.purchase_offer

        sale_quantity_before_trade = sale_offer.quantity
        purchase_quantity_before_trade = purchase_offer.quantity
        
        with transaction.atomic():
            services.offers_trade(sale_offer, purchase_offer)

        sale_quantity_after_trade = sale_offer.quantity
        purchase_quantity_after_trade = purchase_offer.quantity

        instance.status = 'closed'
        instance.purchase_quantity_before_trade = purchase_quantity_before_trade
        instance.sale_quantity_before_trade = sale_quantity_before_trade
        instance.purchase_quantity_after_trade = purchase_quantity_after_trade
        instance.sale_quantity_after_trade = sale_quantity_after_trade