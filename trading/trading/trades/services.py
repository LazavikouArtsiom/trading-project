from trading.offers.models import SaleOffer, PurchaseOffer


def calculate_transaction_quantity(sale_offer, purchase_offer):
    return sorted([sale_offer.quantity, purchase_offer.quantity])[0]


def calcuclate_money(quantity, price):
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

    sale_offer.user.inventory.add_item_quantity(currency=offer_currency,
                                                quantity=quantity,
                                                user=purchase_offer.user)
    sale_offer.user.inventory.remove_item_quantity(currency=offer_currency,
                                                   quantity=quantity,
                                                   user=sale_offer.user)

    sale_offer.remove_quantity(quantity)
    purchase_offer.remove_quantity(quantity)

    close_offers(sale_offer, purchase_offer)


def _search_offers(purchase_offer):
    item = purchase_offer.item
    price = purchase_offer.price
    sale_offer = (SaleOffer.objects
                           .filter(item=item)
                           .filter(price__lte=price)
                           .order_by(price)
                           .first()
                  )
    return sale_offer


def _calculate_money(quantity, price):
    return quantity * price


def _add_money(user, money):
    user.account.money += money


def _remove_money(user, money):
    user.account.money -= money


def _add_shares(user, item, quantity):
    # добавить в inventory_item или создать
    pass


def _remove_shares(user, item, quantity):
    # удалить из inventory_item
    pass


def _close_offers(sale_offer, purchase_offer):
    # return {sale_offer: sale_offer_status,
    #         purchase_offer: purchase_offer_status,
    #         }
    pass


def _send_mail():
    # send email
    pass


def perform_trade(sale_offer, purchase_offer):
    # if sale_offer.quantity > purchase_offer.quantity:
    #     do logic
    # if sale_offer.quantity < purchase_offer.quantity:
    #     do logic
    # if sale_offer.quantity = purchase_offer.quantity:
    #     do logic

    # close_offers(sale_offer, purchase_offer) офферы с количеством 0 закрываются
    pass
