from rest_framework import serializers

from .models import (SaleOffer,
                     PurchaseOffer,
                    )


class SaleOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOffer
        fields = "__all__"


class PurchaseOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOffer
        fields = "__all__"
