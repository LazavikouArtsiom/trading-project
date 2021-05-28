from rest_framework import generics, serializers
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Inventory
from .serializers import InventorySerializer
from .selectors import get_user_inventory


class InventoryRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        return get_user_inventory(self)

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset).data
        return Response(data)

    def post(self, request):
        return Response({'405': 'method not yet implemented'})