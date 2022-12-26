from django.db import models
from django.utils import timezone
import uuid

class Account(models.Model):
    """Account Model"""
    account_id = models.UUIDField(
        primary_key = True, default = uuid.uuid4
    )
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.account_id)

class Transaction(models.Model):
    """Transaction Model"""
    transaction_id = models.UUIDField(
        primary_key = True, default = uuid.uuid4
    )
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="transaction_account")
    amount = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.transaction_id)