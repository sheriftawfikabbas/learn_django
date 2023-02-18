from django.test import LiveServerTestCase
from .models import Transaction
from .forms import TransactionForm
from django.urls import reverse
from django.test import Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TransactionModelTests(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()

    def test_form_elements(self):
        self.selenium.get(self.live_server_url+'/transaction')

        assert 'id_product_code' in self.selenium.page_source
        assert 'id_quantity' in self.selenium.page_source
        assert 'id_price' in self.selenium.page_source

    def test_link_to_report(self):
        self.selenium.get(self.live_server_url+'/transaction')
        a = self.selenium.find_element_by_id('link')
        a.click()
        assert 'POS Report' == self.selenium.title

    def test_entry_1_item(self):
        self.selenium.get(self.live_server_url+'/transaction')

        #Retrieve the form elements based on Django's naming convension
        product_code = self.selenium.find_element_by_id('id_product_code')
        quantity = self.selenium.find_element_by_id('id_quantity')
        price = self.selenium.find_element_by_id('id_price')
        submit = self.selenium.find_element_by_id('submit')

        #populate the form with data
        product_code.send_keys('111')
        quantity.send_keys('1')
        price.send_keys('10')

        #submit form
        submit.send_keys(Keys.RETURN)

        #Check if it was actually saved by checking the report page
        self.selenium.get(self.live_server_url+'/report')
        assert '111' in self.selenium.page_source

    def tearDown(self):
        self.selenium.close()
