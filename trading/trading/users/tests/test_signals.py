from django.test import TestCase
from trading.users.models import User

from trading.inventories.models import Inventory
from trading.accounts.models import Account
from trading.watchlists.models import Watchlist


class SignalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )

    def test_user_signal_had_created_inventory(self):
        self.assertIsNotNone(Inventory.objects.get(user=self.user))
        
    def test_user_signal_had_created_watchlist(self):
        self.assertIsNotNone(Watchlist.objects.get(user=self.user))
        
    def test_user_signal_had_created_account(self):
        self.assertIsNotNone(Account.objects.get(user=self.user))