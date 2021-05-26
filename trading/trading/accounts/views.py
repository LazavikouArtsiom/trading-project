from rest_framework.generics import RetrieveUpdateAPIView

from .models import Account
from .serializers import AccountSerializer

class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    
    def get_queryset(self):
        return Account.objects.get(user=self.request.user)