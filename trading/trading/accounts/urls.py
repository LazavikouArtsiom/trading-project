from django.urls import path

from .views import AccountRetrieveUpdateAPIView

urlpatterns = [
    path('', AccountRetrieveUpdateAPIView.as_view()),
]