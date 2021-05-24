from django.contrib import admin

from .models import SaleOffer, PurchaseOffer

admin.site.register(SaleOffer)
admin.site.register(PurchaseOffer)