from django.urls import path
from rest_framework.routers import SimpleRouter

from trading.trades.viewsets import TradeReadOnlyViewSet


router = SimpleRouter()
router.register(r'history', TradeReadOnlyViewSet, basename='trade')

urlpatterns = router.urls