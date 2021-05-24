from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework.routers import SimpleRouter

from .viewsets import TradeReadOnlyViewSet

router = SimpleRouter()

router.register(r'history', TradeReadOnlyViewSet, basename='trade')

urlpatterns = [

] + router.urls