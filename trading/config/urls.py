from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

user_urlpatterns = [
    path("offers/", include("trading.offers.urls.user_urlpatterns")),
    path("inventory/", include("trading.inventories.urls")),
    path("watchlists/", include("trading.watchlists.urls")),
    path("trades/", include("trading.trades.urls")),
    path("account/", include("trading.accounts.urls")),
]

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("offers/", include("trading.offers.urls.urlpatterns")),
    path("items/", include("trading.items.urls")),
    path("my/", include("user_urlpatterns")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
