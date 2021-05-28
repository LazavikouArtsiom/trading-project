from django.urls import path

from .views import InventoryRetrieve


urlpatterns = [
    path('', InventoryRetrieve.as_view()),
]