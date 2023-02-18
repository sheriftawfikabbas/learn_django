from django.test import TestCase
from .models import Transaction
from .forms import TransactionForm
from django.urls import reverse
from django.test import Client



class TransactionModelTests(TestCase):
    client = Client()

    def test_price_is_valid(self):
        t = Transaction(product_code='', quantity=1, price=-1)
        self.assertIs(t.price_is_valid(), False)

    def test__str__(self):
        t = Transaction(product_code='p1',
                        quantity=1, price=10)
        self.assertEqual(str(t), t.product_code+'_1_10')

    def test_apply_discount(self):
        t = Transaction(product_code='p2',
                        quantity=1, price=10)
        t.apply_discount(10)
        self.assertEqual(t.price, 9)


class TransactionIndexViewTests(TestCase):
    def test_transaction_index_loads_properly(self):
        response = self.client.get(reverse('transaction:index'))
        self.assertEqual(response.status_code, 200)


class TransactionFormTests(TestCase):
    def test_validation_do_not_accept_blanks(self):
        form = TransactionForm(data={})
        self.assertFalse(form.is_valid())
