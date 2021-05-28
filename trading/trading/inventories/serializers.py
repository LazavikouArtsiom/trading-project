from rest_framework import serializers

from trading.items.serializers import CurrencySerializer
from .models import (Inventory, 
                     InventoryItem,
                    )


class InventoryItemSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = InventoryItem
        fields = ['currency', 'quantity']


class InventorySerializer(serializers.ModelSerializer):
    inventory_items = InventoryItemSerializer(read_only=True, many=True)

    class Meta:
        model = Inventory
        fields = ["inventory_items"]
