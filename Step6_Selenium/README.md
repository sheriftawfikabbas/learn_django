This course introduces Selenium as a testing tool for your Django projects. Selenium is quite fun to learn and use: it can make your python program pretend it is an actual user browsing a website, so it is ideal for testing web application. You will use Selenium to test various aspects of a sample Django project. After understanding how the sample project works, your will write Selenium test functions to test the views of the project apps. In particular, you will learn how to test the presence of certain strings in a web page, the presence of form elements, whether a link successfully navigates to the right page, and whether a form is successfully submitted.

Objectives:
Understand how to use Selenium as part of the testing platform in Django
Learn how to test the mechanics of Django views and forms

Tasks: 
Understand the sample Django project and its apps
Setup the project for Selenium testing
Perform basic tests on the view
Test the form elements and links
Test the form submission

Test you Django views and forms using Selenium

Task 1: Understand the sample Django project and its apps

•	Welcome to this guided project about how to “Test you Django views and forms using Selenium.” 
•	My name is Sherif and I will be your instructor for this project. 
•	I am a research fellow in the field of computational physics and I do most of my scientific and business programming in python.
•	This project is for people who are interested in learning the basics of how to test Django web applications using Selenium.
•	Selenium is a third-party software that is design to let your python program pretend it is a user accessing your webapp through an actual web browser. We will see shortly how this is going to look!

•	Now before I start, I would like to note that to get the most out of this project, you should have a basic understanding of Django development. 
•	Are you ready? Let’s get started!


•	I’m excited to teach you Django testing with Selenium, and I hope that skills you will gain from this project will be useful for your quality assurance tasks.


•	Let’s take a bird’s eye view at what you’ll accomplish by the end of this project. 
•	You will understand a basic Django project that contains two Django apps. Each app has a view
•	After that, we will test the view of each app using Selenium.


•	Now, let’s dive right in. 
•	Once you load your cloud desktop, you’ll find the terminal app, the Google Chrome browser and Microsoft Visual Studio Code on the desktop. We will be using these apps throughout the project.


cd Desktop
cd pos
code .

in order to launch Visual Studio code and open the files of the pos project for editing.

The file structure in visual studio code looks like this:


Now let’s run it:

python manage.py runserver

Here is how it works: transaction/report

We are now ready to start testing our Selenium, which we will be doing in our next task!

Great job on completing the first part of this project! In this Task, we navigated the sample Django project and understood how it works.

In the next Task, we’ll pick up where we left off here and we will learn how to setup our project for Selenium testing.

Task 2: Setup the project for Selenium testing

Welcome back!

In this task we are going to learn how to setup our Django project for Selenium testing. 

There are two things we need to install:

The selenium python package
pip3 install selenium

And the Google Chrome driver, which Selenium will operate. For the purpose of this tutorial, we will download the driver and place it in the project directory. This is done in 2 steps:

1-	Check the version of your Google Chrome, like that -> Settings -> About Chrome
2-	Download the relevant file from https://chromedriver.chromium.org/downloads
3-	Place it in the project director

We are now ready to do testing with Selenium!

Task 3: Perform basic tests on the view

Welcome back!

In the third task of this project, we will test the index view in the report app. This app displays the entries that were entered through the transaction view. So there are 2 things we are going to test:

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



Great job on completing the third part of this project! In this Task, we learned how to use Selenium to test the view in the report app.

In the next Task, we’ll pick up where we left off here and we will learn how to test the view in the transaction app.

Task 4: Test the form elements and links

Welcome back!

In the fourth task of this project, we will test the view in the transaction app.

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


Great job on completing the fourth part of this project! In this Task, we learned how to test the view in the transaction app.

In the next and last Task, we’ll pick up where we left off here and we will continue testing the view in the transaction app.

Task 5: Test the form submission

Welcome back!

In the fifth and last task of this project, we will learn how to test form submission in the transaction app.


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

OK, now let’s run our tests!

python3 manage.py test transaction
python3 manage.py test report

Woops we have some issues in our code! Now let’s go and check them, and correct them!

I hope you’ve enjoyed our learning journey, and I wish you will find this learning useful to you. 

One last thing, I would appreciate that you provide your feedback and star rating to my project.

