from rest_framework import viewsets

from trading.offers import selectors
from trading.offers.serializers import (SaleOfferSerializer,
                                        PurchaseOfferSerializer,
                                        )
from trading.offers.models import SaleOffer, PurchaseOffer


class SaleOfferViewSet(viewsets.ModelViewSet):
    serializer_class = SaleOfferSerializer

    def get_queryset(self):
        return selectors.get_opened_sale_offers(self)


class PurchaseOfferViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOfferSerializer

    def get_queryset(self):
        return selectors.get_opened_purchase_offers(self)


class MySaleOfferViewSet(viewsets.ModelViewSet):
    serializer_class = SaleOfferSerializer

    def get_queryset(self):
        return selectors.get_users_sale_offers(self)


class MyPurchaseOfferViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOfferSerializer

    def get_queryset(self):
        return selectors.get_users_purchase_offers(self)
