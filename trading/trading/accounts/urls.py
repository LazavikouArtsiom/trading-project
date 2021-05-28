from django.urls import path

from trading.accounts.views import AccountRetrieveUpdateAPIView


urlpatterns = [
    path('', AccountRetrieveUpdateAPIView.as_view()),
]