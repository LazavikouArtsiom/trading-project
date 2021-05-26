from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Watchlist
from .serializers import WatchlistSerializer


class WatchlistViewSet(ReadOnlyModelViewSet):
    
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.get(user=self.request.user)

    