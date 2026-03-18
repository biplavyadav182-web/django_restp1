from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

@api_view(["GET", "POST"])
def transaction_function(request):
    return Response({
        
    })


class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transaction.objects.all()
        serializers = TransactionsSerializer(queryset, many =True)
        return Response({
        "data" : serializers.data
    })
        
    def post(self, request):
        return Response({
            "message":"this is a post method."
        } 
        )
            
        
    
    def put(self, request):
        return Response({
            "message":"this is a put method."
        })
        
    def patch(self, request):
        return Response({
            "message":"this is a patch method."
        })
        
        