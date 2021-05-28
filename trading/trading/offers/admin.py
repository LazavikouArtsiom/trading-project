from django.contrib import admin

from trading.offers.models import SaleOffer, PurchaseOffer


admin.site.register(SaleOffer)
admin.site.register(PurchaseOffer)