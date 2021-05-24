from rest_framework import generics, serializers
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Watchlist
from .serializers import WatchlistSerializer

class WatchlistRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = WatchlistSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Watchlist.objects.filter(user=user)