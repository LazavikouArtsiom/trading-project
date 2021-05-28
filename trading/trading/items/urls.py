from django.urls import path
from rest_framework import routers

from trading.items.viewsets import CurrencyReadOnlyViewSet


router = routers.SimpleRouter()
router.register('currencies/', CurrencyReadOnlyViewSet, basename='currencies')

urlpatterns = router.urls