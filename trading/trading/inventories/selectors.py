from .models import Inventory


def get_user_inventory(self):
    return Inventory.objects.filter(user=self.kwargs['user'])