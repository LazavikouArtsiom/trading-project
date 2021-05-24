from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WatchlistsConfig(AppConfig):
    name = "trading.watchlists"
    verbose_name = _("Watchlists")

