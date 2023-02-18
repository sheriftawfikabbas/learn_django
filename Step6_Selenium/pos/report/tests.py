from django.test import LiveServerTestCase
from django.urls import reverse
from transaction.models import Transaction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ReportViewTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        
    def test_title(self):
        # Choose your url to visit
        self.selenium.get(self.live_server_url+'/report')
        self.assertEquals(self.selenium.title, "POS Report")

    def test_no_transactions(self):
        self.selenium = webdriver.Chrome()
        # Choose your url to visit
        self.selenium.get(self.live_server_url+'/report')
        html = self.selenium.page_source
        assert "No transactions yet." in html

    def tearDown(self):
        self.selenium.close()
