from rest_framework import serializers

from trading.watchlists.models import Watchlist
from trading.items.serializers import CurrencySerializer


class WatchlistSerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True)

    class Meta:
        model = Watchlist
        fields = ['currencies']



