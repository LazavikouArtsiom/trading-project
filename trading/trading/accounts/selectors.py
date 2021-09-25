from trading.accounts.models import Account


def get_user_account(self):
    return Account.objects.get(user=self.request.user)