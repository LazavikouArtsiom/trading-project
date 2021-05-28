from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from trading.accounts.models import Account
from trading.accounts.serializers import AccountSerializer


class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    
    def get_queryset(self):
        return Account.objects.get(user=self.request.user)

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset).data

        return Response(data)
    
    def post(self, request):
        return Response({'405': 'method not yet implemented'})