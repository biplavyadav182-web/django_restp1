from rest_framework import serializers
from .models import Transaction

class TransactionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        # fields = [
        #     'title',
        #     'amount',
        #     'transaction_type',
        # ]
       
        fields = "__all__"
        
