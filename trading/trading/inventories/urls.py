from django.urls import path

from trading.inventories.views import InventoryRetrieve


urlpatterns = [
    path('', InventoryRetrieve.as_view()),
]