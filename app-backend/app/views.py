from .models import Account
from .serializers import AccountSerializer
from django.db.models import F
from rest_framework import generics
from rest_framework import filters

class AccountListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at']

class AccountDetailsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "account_id"