from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Trade
from .serializers import TradeSerializer
from .selectors import get_trades_list

class TradeReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = TradeSerializer

    def get_queryset(self):
        return get_trades_list(user=self.request.user)