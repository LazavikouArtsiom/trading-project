from rest_framework import serializers

from trading.offers.models import SaleOffer, PurchaseOffer


class PurchaseOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOffer
        fields = ['currency', 'quantity', 'price',
                  'status', 'user', 'id']

    def validate(self, data):
        full_price = data['price'] * data['quantity']
        account_money = data['user'].account.money
        if full_price > account_money:
            raise serializers.ValidationError("You haven't enough money")
        return data


class SaleOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOffer
        fields = ['inventory_item', 'suitable_offers',
                  'quantity', 'price', 'user',
                  'status', 'id'
                  ]

    def validate(self, data):
        item = data['inventory_item']
        item_quantity = item.quantity
        if data['quantity'] > item_quantity:
            raise serializers.ValidationError("You haven't enough items")