from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Account, Transaction

class AccountTests(APITestCase):
    """ Test Account API """
    def setUp(self):
        """ Setup Account """
        self.data = {
            "balance": 2000
        }
        self.response = self.client.post(
            reverse('get_account_list'),
            self.data,
            format='json'
        )

    def test_api_create_account(self):
        """ Create account via api """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().balance, 2000)

    def test_api_list_account(self):
        """ Account list via api """
        url = reverse('get_account_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().balance, 2000)

    def test_api_get_account_detail(self):
        """ Get Account Detail via api """
        account = Account.objects.get()
        response = self.client.get(
            reverse('get_account_detail',
            kwargs={'account_id': account.account_id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, account)


class TransactionTests(APITestCase):
    """ Test Transaction API """
    def setUp(self):
        """ Setup Transaction """
        self.data = {
            "account_id": "a843dbad-9531-45f3-90eb-32615f891a44",
            "amount": 100
        }
        self.response = self.client.post(
            reverse('get_transaction_list'),
            self.data,
            format='json'
        )

    def test_api_create_transaction(self):
        """ Create transaction via api """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().amount, 100)

    def test_api_list_transaction(self):
        """ Transaction list via api """
        url = reverse('get_transaction_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().amount, 100)
        self.assertEqual(Transaction.objects.get().account_id.balance, 100)

    def test_api_get_transaction_detail(self):
        """ Get transaction Detail via api """
        transaction = Transaction.objects.get()
        response = self.client.get(
            reverse('get_transaction_detail',
            kwargs={'transaction_id': transaction.transaction_id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, transaction)

    def test_api_transaction_account_detail(self):
        """ Get Account Balance after few transactions """
        account_id = "a843dbad-9531-45f3-90eb-32615f891a44"

        # Add New Transaction
        self.data = {
            "account_id": account_id,
            "amount": 500
        }
        self.response = self.client.post(
            reverse('get_transaction_list'),
            self.data,
            format='json'
        )
        self.assertEqual(Transaction.objects.count(), 2)
        self.assertEqual(Account.objects.get().balance, 600)

        # Add New Transaction
        self.data = {
            "account_id": account_id,
            "amount": -200
        }
        self.response = self.client.post(
            reverse('get_transaction_list'),
            self.data,
            format='json'
        )
        self.assertEqual(Transaction.objects.count(), 3)
        self.assertEqual(Account.objects.get().balance, 400)