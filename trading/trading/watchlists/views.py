from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from trading.items.models import Currency
from trading.watchlists.models import Watchlist
from trading.watchlists.serializers import WatchlistSerializer


class WatchlistRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        user = self.request.user
        return Watchlist.objects.get(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset).data
        return Response(data)
