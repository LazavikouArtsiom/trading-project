from .models import Inventory


def get_user_inventory(self):
    return Inventory.objects.get(user=self.request.user)