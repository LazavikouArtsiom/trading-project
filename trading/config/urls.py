from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from trading.offers.urls import user_urlpatterns as user_offers_urls
from trading.offers.urls import urlpatterns as common_offers_urls


user_urlpatterns = [
    path("offers/", include(user_offers_urls)),
    path("inventory/", include("trading.inventories.urls")),
    path("watchlist/", include("trading.watchlists.urls")),
    path("trades/", include("trading.trades.urls")),
    path("account/", include("trading.accounts.urls")),
]

apipatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path("offers/", include(common_offers_urls)),
    path("", include("trading.items.urls")),
    path("me/", include(user_urlpatterns)),
]

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/', include(apipatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
