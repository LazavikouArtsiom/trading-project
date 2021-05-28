from rest_framework import serializers

from trading.items.models import Currency
                    

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'code']