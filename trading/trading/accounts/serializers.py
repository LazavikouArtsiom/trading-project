from django.db import models
from rest_framework import serializers

from trading.accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['money']
