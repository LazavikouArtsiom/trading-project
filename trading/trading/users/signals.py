from django.db import transaction

from trading.inventories.models import Inventory
from trading.watchlists.models import Watchlist
from trading.accounts.models import Account


def create_related_to_user_models_postsave(sender, instance, created, **kwargs):
    if not instance.created:
        with transaction.atomic():
            Inventory.objects.create(user=instance)
            Watchlist.objects.create(user=instance)
            Account.objects.create(user=instance)
            instance.created = True
            instance.save()