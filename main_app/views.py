from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Sum


@api_view(["GET", "POST"])
def transaction_function(request):
    return Response({
        
    })


class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-id')
        serializers = TransactionsSerializer(queryset, many =True)
        total = queryset.aggregate(total = Sum('amount')) ['total'] or 0
        return Response({
        "data" : serializers.data,
        "total": total
    })
        
    def post(self, request):
        data = request.data
        serializers = TransactionsSerializer(data=data)
        
        if not serializers.is_valid():
            return Response({
                "message":"data not saved",
                "errors":serializers.errors, 
            })
        serializers.save()
        return Response({
            "message":"data saved",
            "data": serializers.data
        })
        
        
            
        
    
    def put(self, request):
        return Response({
            "message":"this is a put method."
        })
        
        
        
        
    def patch(self, request):
        
        data = request.data
        if not data.get('id'):
            return Response({
                "message":"data not updated",
                "errors":"id is required",
            })
            
        transaction = Transaction.objects.get(id=data.get('id'))
        serializers = TransactionsSerializer(transaction, data=data, partial=True)
        
        if not serializers.is_valid():
            return Response({
                "message":"wrong xa",
                "erros":"id is required",
            })
        serializers.save()
        return Response({
            "message":"this is a patch method.",
            "data":serializers.data
        })
        
        
    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message":"data not updated",
                "errors":"id is required",
            })
            
        transaction = Transaction.objects.get(id = data.get('id')).delete()
        
        return Response({
            "message":"data deleted",
            "data" : {}
        })
        
        