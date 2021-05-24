from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TradeSerializer
from .models import Trade


class TradeHistoryAPIView(APIView):
    
    def get(self, request):
        queryset = Trade.objects.filter(user=request.user)
        data = TradeSerializer(data=queryset, many=True).data

        return Response(data)


class TradeHistoryItemAPIView(APIView):
    
    def get(self, request, id):
        queryset = Trade.objects.filter(user=request.user).filter(id=id)
        data = TradeSerializer(data=queryset).data

        return Response(data)
        
