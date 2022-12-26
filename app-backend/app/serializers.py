from rest_framework import serializers
from .models import Account, Transaction
from django.db.models import F

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["account_id", "balance", "created_at"]

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["transaction_id", "account_id", "amount", "created_at"]
        read_only_fields = ['account_id']