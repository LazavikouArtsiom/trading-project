from django.test import TestCase
from trading.users.models import User

from trading.accounts.models import Account


class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password',
                                        )
        self.account = Account.objects.get(user=self.user)
        self.account.money = 100
        self.account.save()

    def test_add_money(self):
        self.account.add_money(100)
        self.account.save()
        self.assertEqual(self.account.money, 200)

    def test_add_money(self):
        self.account.remove_money(90)
        self.account.save()
        self.assertEqual(self.account.money, 10)
