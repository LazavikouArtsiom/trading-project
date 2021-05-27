from trading.offers.models import SaleOffer, PurchaseOffer


def calculate_transaction_quantity(sale_offer, purchase_offer):
    return sorted([sale_offer.quantity, purchase_offer.quantity])[0]


def calcuclate_money(quantity: int, price: int):
    return quantity * price


def close_offers(sale_offer, purchase_offer):
    '''
    Logic for closing offers after Trade is complete
    '''
    for offer in [sale_offer, purchase_offer]:
        if offer.quantity == 0:
            offer.set_status('closed')


def offers_trade(sale_offer, purchase_offer):

    quantity = calculate_transaction_quantity(sale_offer, purchase_offer)

    offer_money = calcuclate_money(quantity, purchase_offer.price)
    offer_currency = purchase_offer.currency

    sale_offer.user.account.add_money(offer_money)
    purchase_offer.user.account.remove_money(offer_money)

    purchase_offer.user.inventory.add_item_quantity(currency=offer_currency,
                                                quantity=quantity,
                                                user=purchase_offer.user)
    sale_offer.user.inventory.remove_item_quantity(currency=offer_currency,
                                                   quantity=quantity,
                                                   user=sale_offer.user)

    sale_offer.remove_quantity(quantity)
    purchase_offer.remove_quantity(quantity)

    close_offers(sale_offer, purchase_offer)
