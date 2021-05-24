from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ItemsConfig(AppConfig):
    name = "trading.items"
    verbose_name = _("Items")

