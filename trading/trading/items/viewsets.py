from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyReadOnlyViewSet(ReadOnlyModelViewSet):
    model = Currency
    serializer_class = CurrencySerializer
    