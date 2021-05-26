from rest_framework import viewsets
from rest_framework.decorators import action

from .models import (SaleOffer, 
                     PurchaseOffer,
                     )
from .serializers import (SaleOfferSerializer,
                          PurchaseOfferSerializer,
                          )
from .selectors import (get_users_purchase_offers,  
                        get_users_sale_offers,
                       )


class SaleOfferViewSet(viewsets.ModelViewSet):

    serializer_class = SaleOfferSerializer
    queryset = SaleOffer.objects.all()


class PurchaseOfferViewSet(viewsets.ModelViewSet):

    serializer_class = PurchaseOfferSerializer
    queryset = PurchaseOffer.objects.all()


class MySaleOfferViewSet(viewsets.ModelViewSet):

    serializer_class = SaleOfferSerializer

    def get_queryset(self):
        return get_users_sale_offers(self)
    

class MyPurchaseOfferViewSet(viewsets.ModelViewSet):

    serializer_class = PurchaseOfferSerializer

    def get_queryset(self):
        return get_users_purchase_offers(self)