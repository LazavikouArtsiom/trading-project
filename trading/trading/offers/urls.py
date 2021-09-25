from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework import routers

from trading.offers.viewsets import (SaleOfferViewSet,
                       PurchaseOfferViewSet,
                       MySaleOfferViewSet,
                       MyPurchaseOfferViewSet,
                      )


router = routers.SimpleRouter()
user_router = routers.SimpleRouter()

router.register(r'sale', SaleOfferViewSet, basename='offers_sale')
router.register(r'purchase', PurchaseOfferViewSet, basename='offers_purchase')

user_router.register(r'purchase', MyPurchaseOfferViewSet, basename='user_offers_purchase')
user_router.register(r'sale', MySaleOfferViewSet, basename='user_offers_purchase')


user_urlpatterns = user_router.urls

urlpatterns = router.urls