from rest_framework import generics, serializers
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from trading.inventories.models import Inventory
from trading.inventories.serializers import InventorySerializer
from trading.inventories import selectors


class InventoryRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        return selectors.get_user_inventory(self)

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset).data
        return Response(data)
