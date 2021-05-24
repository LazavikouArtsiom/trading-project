from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Trade
from .serializers import TradeSerializer

class TradeReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = TradeSerializer

    def get_queryset(self):
        user = self.request.user
        return Trade.objects.filter(purchase_offer__user=user).filter(sale_offer__user=user)