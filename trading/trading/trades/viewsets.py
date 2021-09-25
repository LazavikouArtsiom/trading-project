from rest_framework.viewsets import ReadOnlyModelViewSet

from trading.trades.models import Trade
from trading.trades.serializers import TradeSerializer
from trading.trades import selectors


class TradeReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = TradeSerializer

    def get_queryset(self):
        return selectors.get_trades_list(user=self.request.user)