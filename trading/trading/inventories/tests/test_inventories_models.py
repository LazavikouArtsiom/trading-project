from django.test import TestCase
from trading.users.models import User

from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency


class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.inventory = Inventory.objects.get(user=self.user)
        self.currency = Currency.objects.create(code='AAPL',
                                                name='apple',)
        self.inventory_item = InventoryItem.objects.create(currency=self.currency, user=self.user, quantity=10)
        self.inventory.inventory_items.add(self.inventory_item)
        self.inventory.save()

    def test_add_item_quantity(self):
        self.inventory.add_item_quantity(currency=self.currency, quantity=10, user=self.user)
        self.inventory.save()
        inventory_item = self.inventory.inventory_items.get(currency=self.currency, user=self.user)
        quantity = inventory_item.quantity
        self.assertEqual(quantity, 20)

    def test_remove_item_quantity(self):
        self.inventory.remove_item_quantity(currency=self.currency, quantity=9, user=self.user)
        self.inventory.save()
        inventory_item = self.inventory.inventory_items.get(currency=self.currency, user=self.user)
        quantity = inventory_item.quantity
        self.assertEqual(quantity, 1)
