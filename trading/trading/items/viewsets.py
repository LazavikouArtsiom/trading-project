from rest_framework.viewsets import ReadOnlyModelViewSet

from trading.items.models import Currency
from trading.items.serializers import CurrencySerializer


class CurrencyReadOnlyViewSet(ReadOnlyModelViewSet):
    model = Currency
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()