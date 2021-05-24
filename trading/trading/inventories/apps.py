from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InventoriesConfig(AppConfig):
    name = "trading.inventories"
    verbose_name = _("Inventories")

