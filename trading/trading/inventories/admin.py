from django.contrib import admin

from trading.inventories.models import Inventory, InventoryItem


admin.site.register(Inventory)
admin.site.register(InventoryItem)