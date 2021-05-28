from trading.offers.models import SaleOffer, PurchaseOffer


def get_sale_offers():
    return (SaleOffer
            .objects
            .filter(status='opened')
            .order_by('datetime_created')
            )


def get_suitable_offers(id: int):
    offer = SaleOffer.objects.get(id=id)
    return (PurchaseOffer
            .objects
            .filter(price__gte=offer.price)
            .filter(status='opened')
            .exclude(user=offer.user)
            .exclude(quantity=0)
            .order_by('price', 'datetime_created')
            )


def get_users_purchase_offers(self):
    return PurchaseOffer.objects.filter(user=self.request.user).filter(status="opened")


def get_users_sale_offers(self):
    return SaleOffer.objects.filter(user=self.request.user).filter(status="opened")


def get_opened_purchase_offers(self):
    return PurchaseOffer.objects.filter(status="opened").order_by('price', 'datetime_created')


def get_opened_sale_offers(self):
    return SaleOffer.objects.filter(status="opened").order_by('price', 'datetime_created')
