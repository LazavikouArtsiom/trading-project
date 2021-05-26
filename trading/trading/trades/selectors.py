from .models import Trade

def get_trades_list(user):
    return Trade.objects.filter(purchase_offer__user=user).filter(sale_offer__user=user)