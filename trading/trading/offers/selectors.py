from .models import SaleOffer, PurchaseOffer


def get_sale_offers():
    return (SaleOffer
                    .objects
                    .filter(status='opened')
                    .order_by('datetime_created')
            )


def get_suitable_offers(offer):
    return (PurchaseOffer
                        .objects
                        .filter(price__gte=offer.price)
                        .filter(status='opened')
                        .exclude(user=offer.user)
                        .order_by('price')
            )
