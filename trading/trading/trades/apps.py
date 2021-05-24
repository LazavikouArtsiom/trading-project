from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TradesConfig(AppConfig):
    name = "trading.trades"
    verbose_name = _("Trades")

