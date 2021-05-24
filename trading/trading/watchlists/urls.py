from re import I
from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework import routers

from .views import WatchlistRetrieveUpdate

urlpatterns = [
    path('', WatchlistRetrieveUpdate.as_view()),
]