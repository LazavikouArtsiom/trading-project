from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework import routers

from .viewsets import (SaleOfferViewSet,
                       PurchaseOfferViewSet,
                      )

router = routers.SimpleRouter()

router.register(r'sale', SaleOfferViewSet, basename='offers_sale')
#offers/sale
#offers/sale/id/
#offers/sale/id/buy
router.register(r'purchase', PurchaseOfferViewSet, basename='offers_purchase')
#offers/purchase
#offers/purchase/id
#offers/purchase/id/sale


urlpatterns = [
    #offers/my
    #offers/my/purchase
    #offers/my/purchase/id
    #offers/my/sale
    #offers/my/sale/id
] + router.urls