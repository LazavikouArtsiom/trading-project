from django.urls import path
from rest_framework import routers

from trading.watchlists.views import WatchlistRetrieveUpdate


urlpatterns = [
    path('', WatchlistRetrieveUpdate.as_view()),
]