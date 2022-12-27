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

class Category(models.Model):
    """Category Model"""
    category_name = models.CharField(max_length=512)
    category_image = models.CharField(max_length=2096, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.category_name)

class Choice(models.Model):
    """Choice Model"""
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="choice_category")
    choice_name = models.CharField(max_length=512)
    choice_image = models.CharField(max_length=2096, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.choice_name)

class Guest(models.Model):
    """Guest Model"""
    guest_name = models.CharField(max_length=512)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.guest_name)

class Result(models.Model):
    """Result Model"""
    choice_id = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name="result_choice")
    guest_id = models.ForeignKey(Guest, on_delete=models.PROTECT, related_name="result_guest")
    elo_rating = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return Value."""
        return str(self.elo_rating)