from django.test import TestCase

from trading.users.models import User
from trading.inventories.models import Inventory, InventoryItem
from trading.items.models import Currency
from trading.offers.models import SaleOffer, PurchaseOffer

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
        self.sale_offer_1 = SaleOffer.objects.create(
            inventory_item=self.inventory_item, quantity=0, price=10, user=self.user)
        self.purchase_offer = PurchaseOffer.objects.create(
            currency=self.currency, quantity=5, price=10, user=self.user_1)

    def test_calculate_money(self):
        money = calcuclate_money(10, 100)
        self.assertEqual(money, 1000)

    def test_calculate_transaction_quantity(self):
        transaction_quantity = calculate_transaction_quantity(self.sale_offer, self.purchase_offer)
        self.assertEqual(transaction_quantity, 5)

    def test_close_offers(self):
        close_offers(self.sale_offer_1, self.purchase_offer)
        self.assertEqual(self.sale_offer_1.status, 'closed')
        self.assertEqual(self.purchase_offer.status, 'opened')

    def test_offers_trade(self):
        offers_trade(sale_offer=self.sale_offer, purchase_offer=self.purchase_offer)
        self.assertEqual(self.user.account.money, 50)
        self.assertEqual(self.user_1.account.money, 950)
        self.assertEqual(self.sale_offer.status, 'opened')
        self.assertEqual(self.purchase_offer.status, 'closed')
        self.assertEqual(self.purchase_offer.quantity, 0)
        self.assertEqual(self.sale_offer.quantity, 5)

        user_inventory_item = self.user.inventory.inventory_items.get(currency=self.currency, user=self.user)
        user_1_inventory_item = self.user_1.inventory.inventory_items.get(currency=self.currency, user=self.user_1)   

        self.assertEqual(user_inventory_item.quantity, 5)    
        self.assertEqual(user_1_inventory_item.quantity, 5)    
