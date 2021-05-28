from rest_framework import generics, serializers
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Inventory
from .serializers import InventorySerializer
from .selectors import get_user_inventory


class InventoryRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        return get_user_inventory(self)