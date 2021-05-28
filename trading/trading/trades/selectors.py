from django.db.models import Q

from .models import Trade


def get_trades_list(user):
    return Trade.objects.filter(Q(purchase_offer__user=user)|Q(sale_offer__user=user))
