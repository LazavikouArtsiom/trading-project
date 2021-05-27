from django.test import TestCase

from trading.users.models import User
from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency
from trading.offers.models import SaleOffer, PurchaseOffer


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
        self.sale_offer = SaleOffer.objects.create(
            inventory_item=self.inventory_item, quantity=10, price=10, user=self.user)
        self.purchase_offer = PurchaseOffer.objects.create(
            currency=self.currency, quantity=5, price=10, user=self.user)

    def test_remove_quantity(self):
        self.sale_offer.remove_quantity(quantity=3)
        sale_offer_quantity = self.sale_offer.quantity
        self.purchase_offer.remove_quantity(quantity=3)
        purchase_offer_quantity = self.purchase_offer.quantity
        self.assertEqual(sale_offer_quantity, 7)
        self.assertEqual(purchase_offer_quantity, 2)
