from django.urls import path
from rest_framework import routers

from .viewsets import CurrencyReadOnlyViewSet

router = routers.SimpleRouter()

router.register('currencies/')

urlpatterns = [
] + router.urls