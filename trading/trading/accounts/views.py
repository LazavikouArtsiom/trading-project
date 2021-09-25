from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from trading.accounts.models import Account
from trading.accounts.serializers import AccountSerializer
from trading.accounts import selectors


class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    
    def get_queryset(self):
        return selectors.get_user_account(self)

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset).data

        return Response(data)
