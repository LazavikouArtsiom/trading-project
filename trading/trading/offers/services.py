from .selectors import get_suitable_offers


def add_suitable_offers_into_field(offer):
    purchase_offers = list(get_suitable_offers(offer.id))

    offer.suitable_offers.add(*purchase_offers)
    offer.save()