from rest_framework import serializers

from trading.trades.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['status', 'sale_offer', 'purchase_offer',
                  'purchase_quantity_before_trade', 
                  'purchase_quantity_after_trade',
                  'sale_quantity_before_trade',
                  'sale_quantity_after_trade',
                  ]

    def validate(self, data):
        sale_offer = data['sale_offer'] 
        purchase_offer = data['purchase_offer'] 

        if sale_offer.user == purchase_offer.user:
            raise serializers.ValidationError("Sale offer user can't be the same as purchase offer user")

        return data
