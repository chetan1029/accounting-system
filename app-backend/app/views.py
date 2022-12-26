from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer
from django.db.models import F
from rest_framework import generics
from rest_framework import filters
from django.db import transaction
from django.http import JsonResponse

def ping(request):
    return JsonResponse({"result": "pong"})

class AccountListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at']

class AccountDetailsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "account_id"

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at']

    def perform_create(self, serializer):
        with transaction.atomic():
            account_id = self.request.data.get("account_id", None)
            amount = self.request.data.get("amount", None)
            try:
                account, created = Account.objects.get_or_create(account_id=account_id)
                account.balance = F('balance') + amount
                account.save()
                serializer.save(account_id=account)
            except:
                pass
            return super().perform_create(serializer)

class TransactionDetailsView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "transaction_id"