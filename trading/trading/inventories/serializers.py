from rest_framework import serializers

from .models import (Inventory, 
                     InventoryItem,
                    )


class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        fields = ['currency', 'quantity']


class InventorySerializer(serializers.ModelSerializer):
    inventory_items = InventoryItemSerializer(read_only=True, many=True)

    class Meta:
        model = Inventory
        fields = ["inventory_items"]
