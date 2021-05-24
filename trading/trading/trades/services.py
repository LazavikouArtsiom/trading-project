from offers.models import SaleOffer, PurchaseOffer

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
    #send email
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

