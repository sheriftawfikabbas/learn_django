import unittest
from django.test import TestCase, override_settings
from .models import Transaction
from .forms import TransactionForm
from django.urls import reverse
from django.test import Client
from http import HTTPStatus
from bs4 import BeautifulSoup
from django.conf import settings



class TransactionIndexViewTests(TestCase):
    # Task 2
    fixtures = ['transactions.json']

    # Task 2
    def test_fixture(self):
        self.assertEqual(len(Transaction.objects.all()), 2)

    # Task 3
    def test_url_setting(self):
        with self.settings(TRANSACTION_URL='trx'):
            response = self.client.get(
                reverse(settings.TRANSACTION_URL + ':index'))
            self.assertEqual(response.status_code, 200)

    @override_settings(TRANSACTION_URL='trx')
    def test_url_setting_with_decorator(self):
        response = self.client.get(
            reverse(settings.TRANSACTION_URL + ':index'))
        self.assertEqual(response.status_code, 200)

    # Task 4
    def test_invalid_form_submission(self):
        response = self.client.post(
            "/transaction/", data={}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Transaction.objects.all()), 2)

    # Task 5
    def test_valid_form_submission(self):
        response = self.client.post(
            "/transaction/", data={"product_code": "p123", "quantity": 1, "price": 10}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Transaction.objects.all()), 3)
        self.assertIn("POS", str(response.content))
        self.assertContains(response, "POS", 1)

    # Task 5
    def test_count_of_transactions_in_report(self):
        response = self.client.get(reverse('report:index'))
        self.assertContains(response, "POS Report", 1)
        self.assertContains(response, "<li>", 2)

    # Task 6
    def test_html(self):
        response = self.client.get(reverse('report:index'))
        soup = BeautifulSoup(str(response.content))
        li = soup.find_all('li')[0]
        self.assertHTMLEqual(str(li), '<li>Laptop_2_1000.0</li>')
        self.assertInHTML('<li>Laptop_2_1000.0</li>', str(response.content))

    # Task 7
    @unittest.skip("This will be skipped")
    def test_skipping(self):
        self.assertEqual("This test must be skipped", "This test should be skipped")
    
    def test_skipping_within(self):
        self.skipTest("Will skip this test too")
        self.assertEqual("This test must be skipped", "This test should be skipped")
        


    