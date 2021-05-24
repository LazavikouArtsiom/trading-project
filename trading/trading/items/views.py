from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Currency
from .serializers import CurrencySerializer


class CurrencyRetrieveAPIView(APIView):
    
    def get(self, request):
        queryset = Currency.objects.filter(id=id)
        data = CurrencySerializer(data=queryset).data

        return Response(data)


class CurrencyListAPIView(APIView):
    
    def get(self, request, id):
        queryset = Currency.objects.all()
        data = CurrencySerializer(data=queryset, many=True).data

        return Response(data)
        
