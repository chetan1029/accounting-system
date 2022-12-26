from django.test import TestCase
from ..models import Account, Transaction
import uuid
from django.core.exceptions import ValidationError

class AccountTest(TestCase):
    """ Test Account Model """

    def setUp(self):
        """ Setup some account data. """
        self.account = Account.objects.create(balance=1000)

    def test_account_id_valid(self):
        """ Test if account id is valid UUID V4"""
        obj = self.account
        self.assertTrue(obj.account_id)
        self.assertTrue(isinstance(obj.account_id, uuid.UUID))
        self.assertEquals(obj.account_id.version, 4)

    def test_account_id_invalid(self):
        """ Test if account id is invalid UUID V4"""
        with self.assertRaises(ValidationError):
            Account.objects.create(account_id="g8b23814-bcd0-4523-99f9-bdb900e1b4ef", balance=1000)

    def test_account_id_valid_manual(self):
        """ Test if account id is valid UUID V4 by user input"""
        obj = Account.objects.create(account_id="a843dbad-9531-45f3-90eb-32615f891a44", balance=1000)
        self.assertTrue(obj.account_id)
        self.assertEquals(obj.account_id, "a843dbad-9531-45f3-90eb-32615f891a44")

    def test_balance(self):
        """ Test if Balance match """
        obj = self.account
        self.assertTrue(obj.balance)
        self.assertEquals(obj.balance, 1000)

    def test_update_balance(self):
        """ Test balance after update """
        obj = self.account
        obj.balance = obj.balance + 100
        obj.save()
        self.assertEquals(obj.balance, 1100)
        obj.balance = obj.balance - 100
        obj.save()
        self.assertEquals(obj.balance, 1000)

class TransactionTest(TestCase):
    """ Test Transaction Model """

    def setUp(self):
        """ Setup some Transaction data. """
        self.account = Account.objects.create(balance=1000)
        self.transaction = Transaction.objects.create(account_id=self.account, amount=100)
        self.transaction1 = Transaction.objects.create(account_id=self.account, amount=-100)

    def test_transaction_id_valid(self):
        """ Test if transaction id is valid UUID V4"""
        obj = self.transaction
        self.assertTrue(obj.transaction_id)
        self.assertTrue(isinstance(obj.transaction_id, uuid.UUID))
        self.assertEquals(obj.transaction_id.version, 4)

    def test_transaction_account_id_invalid(self):
        """ Test if transaction account id is not instead of account"""
        with self.assertRaises(ValueError):
            Transaction.objects.create(account_id="j843dbad-9531-45f3-90eb-32615f891a44", amount=100)

    def test_transaction_id_invalid(self):
        """ Test if transaction id is invalid UUID V4"""
        with self.assertRaises(ValidationError):
            Transaction.objects.create(transaction_id="j843dbad-9531-45f3-90eb-32615f891a44", account_id=self.account, amount=100)

    def test_transactiont_id_valid_manual(self):
        """ Test if transaction id is valid UUID V4 by user input"""
        obj = Transaction.objects.create(transaction_id="a843dbad-9531-45f3-90eb-32615f891a44", account_id=self.account, amount=1000)
        self.assertTrue(obj.transaction_id)
        self.assertEquals(obj.transaction_id, "a843dbad-9531-45f3-90eb-32615f891a44")

    def test_transaction_amount(self):
        """ Test if transaction amount match """
        obj = self.transaction
        self.assertTrue(obj.amount)
        self.assertEquals(obj.amount, 100)

    def test_negative_transaction_amount(self):
        """ Test if negative transaction amount match """
        obj = self.transaction1
        self.assertTrue(obj.amount)
        self.assertEquals(obj.amount, -100)