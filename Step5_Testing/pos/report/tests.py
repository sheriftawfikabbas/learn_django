from django.test import TestCase
from django.urls import reverse
from transaction.models import Transaction


class ReportIndexViewTests(TestCase):
    def test_report_index_loads_properly(self):
        response = self.client.get(reverse('report:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_transactions(self):
        response = self.client.get(reverse('report:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No transactions yet.")
        self.assertQuerysetEqual(response.context['transactions'], [])

    def test_1_transaction(self):
        t = Transaction(product_code='', price=10, quantity=1)
        t.save()
        response = self.client.get(reverse('report:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No transactions yet.")
        self.assertEqual(len(response.context['transactions']), 1)
