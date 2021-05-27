from django.test import TestCase

from trading.users.models import User
from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency
from trading.offers.models import SaleOffer, PurchaseOffer
from trading.trades.models import Trade

from trading.trades.services import (calcuclate_money,
                                     calculate_transaction_quantity,
                                     offers_trade,
                                     close_offers,)


class ServicesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.user_1 = User.objects.create(username='username_1',
                                          password='password',
                                          )

        self.inventory = Inventory.objects.get(user=self.user)
        self.inventory_1 = Inventory.objects.get(user=self.user_1)

        self.currency = Currency.objects.create(code='AAPL',
                                                name='apple',)

        self.inventory_item = InventoryItem.objects.create(currency=self.currency, user=self.user, quantity=10)
        self.inventory_item_1 = InventoryItem.objects.create(currency=self.currency, user=self.user_1, quantity=0)

        self.inventory.inventory_items.add(self.inventory_item)
        self.inventory.save()

        self.inventory_1.inventory_items.add(self.inventory_item_1)
        self.inventory_1.save()

        self.user_1.account.money = 1000
        self.user_1.save()

        self.sale_offer = SaleOffer.objects.create(
            inventory_item=self.inventory_item, quantity=10, price=10, user=self.user)
        self.purchase_offer = PurchaseOffer.objects.create(
            currency=self.currency, quantity=5, price=10, user=self.user_1)

        self.trade = Trade.objects.create(sale_offer=self.sale_offer,
                                          purchase_offer=self.purchase_offer)
        
    def test_right_quantity_calculation(self):
        self.assertEqual(self.trade.purchase_quantity_before_trade, 5)
        self.assertEqual(self.trade.sale_quantity_before_trade, 10)
        self.assertEqual(self.trade.purchase_quantity_after_trade, 0)
        self.assertEqual(self.trade.sale_quantity_after_trade, 5)

