from django.urls import path
from rest_framework import routers

from .views import WatchlistRetrieveUpdate


urlpatterns = [
    path('', WatchlistRetrieveUpdate.as_view()),
]