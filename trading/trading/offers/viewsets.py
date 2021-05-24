from rest_framework import viewsets
from rest_framework.decorators import action

from .models import (SaleOffer, 
                     PurchaseOffer,
                     )
from .serializers import (SaleOfferSerializer,
                          PurchaseOfferSerializer,
                          )


class SaleOfferViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = SaleOfferSerializer
    queryset = SaleOffer.objects.all()

    @action(detail=True,
            methods=['post'],
            name='subscribe',
            )
    def buy(self, request, pk=None):
        pass


class PurchaseOfferViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PurchaseOfferSerializer
    queryset = PurchaseOffer.objects.all()

    @action(detail=True,
            methods=['post'],
            name='subscribe',
            )
    def sale(self, request, pk=None):
        pass
