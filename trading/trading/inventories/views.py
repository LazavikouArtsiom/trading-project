from rest_framework import generics, serializers
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Inventory
from .serializers import InventorySerializer


class InventoryRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        return Inventory.objects.filter(user=self.kwargs['user'])