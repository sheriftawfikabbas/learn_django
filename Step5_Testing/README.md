Objectives:
Learn how to test the various components of a Django app
Learn how to synchronize development and testing
Practice improving your code based on the results of the tests

Apply basic testing for your Django web application

Task 1: Create the POS Django project and its apps, and set it up for testing

•	Welcome to this guided project about how to “Apply basic testing for your Django web application.” 
•	My name is Sherif and I will be your instructor for this project. 
•	I am a research fellow in the field of computational physics and I do most of my programming in python. 
•	This project is for people who are interested in learning the basics of how to test Django web applications.
•	I’ll teach you the basics of how to test the Django models, views and forms.
•	I would like to note that to get the most out of this project, you should have a basic understanding of Django development. 
•	Are you ready? Let’s get started!


•	I’m excited to teach you Django testing, and I hope that skills you will gain from this project will be useful for your quality assurance tasks.


•	Let’s take a bird’s eye view at what you’ll accomplish by the end of this project. 
•	You will generate a new Django project, and apply testing one method at a time. 
•	I mean that we will be creating each method in the model, view and form and write the corresponding test for it, one at a time. 
•	Following this approach generally ensures that our code is thoroughly tested and quite robust.


•	In this project we will be performing unit tests.
•	We will be writing test functions to test individual instructions, and we will perform integration tests, in which the test function will test the combined operation of multiple components of our web application.

•	An important question that developers will always ask themselves: what should I test? 
o	You should test all aspects of your own code, but not any libraries or functionality provided as part of Python or Django.
o	There are so many things you’d want to test in a Django project. Just like in any web app you want to test the validation of form data, the styling and layout of your pages, whether a page loads successfully, whether a form submits, as well as many other things. 
o	Here we will be doing a bit of each of these in an incremental fashion: we will writing the functionality along with its test, each at a time.

•	Now, let’s dive right in. 
•	Once you load your cloud desktop, you’ll find the terminal app, the Google Chrome browser and Microsoft Visual Studio Code on the desktop. We will be using these apps throughout the project.


cd Desktop
django-admin startproject pos
cd pos
python3 manage.py startapp transaction
python3 manage.py startapp report
code .

in order to launch Visual Studio code and open the files of the pos project for editing.

The file structure in visual studio code looks like this:


Now that we have created a project, let’s run it:

python manage.py runserver

Now let us create the following in our project:
•	Setup the URLs
•	Create our model
•	Create blank index views

We are now ready to start testing our model, which we will be doing in our next task!

Great job on completing the first part of this project! In this Task, we created a basic Django project, sat up the URLs and created blank views.

In the next Task, we’ll pick up where we left off here and we will learn how to test our model.

Task 2: Test the model methods

Welcome back!

In the second task of this project, we are going to learn how to test the methods of the Transaction model.

Method	Checks that	New in
assertEqual(a, b)
a == b	
assertNotEqual(a, b)
a != b	
assertTrue(x)
bool(x) is True	
assertFalse(x)
bool(x) is False	
assertIs(a, b)
a is b	3.1
assertIsNot(a, b)
a is not b	3.1
assertIsNone(x)
x is None	3.1
assertIsNotNone(x)
x is not None	3.1
assertIn(a, b)
a in b	3.1
assertNotIn(a, b)
a not in b	3.1
assertIsInstance(a, b)
isinstance(a, b)	3.2
assertNotIsInstance(a, b)
not isinstance(a, b)	3.2


Method:
def price_is_valid(self):
        if self.price < 0:
            return False
        else:
            return True

Test:
 def test_price_is_valid(self):
        t = Transaction(product_code='', quantity=1, price=-1)
        self.assertIs(t.price_is_valid(), False)

Method:
def __str__(self):
        return self.product_code+'_'+str(self.quantity)+'_'+str(self.price)

Test:
 def test__str__(self):
        t = Transaction(product_code='p1',
                        quantity=1, price=10)
        self.assertEqual(str(t), t.product_code+'_1_10')

Method:
def apply_discount(self, discount):
        self.price = self.price - self.price*discount/100

Test:
def test_apply_discount(self):
        t = Transaction(product_code='p2',
                        quantity=1, price=10)
        t.apply_discount(10)
        self.assertEqual(t.price, 9)



Task 3: Test the transaction app view

Welcome back!

In the third task of this project, we will develop and test the view in the Transaction app.

First, we will create our form mode, which is pretty simple:


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'



Second, we will create our index view function:


def index(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionForm()
    return render(request, 'transaction/index.html', {'form': form})


Finally for the view, we need a simple template:

<html>

<head>
    <title>POS</title>
</head>

<body>
    <form action="{% url 'transaction:index' %}" method="post">
        {% csrf_token %} {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>
</body>

</html>


Now, let’s test if the view is going to load:


class TransactionIndexViewTests(TestCase):
    def test_transaction_index_loads_properly(self):
        response = self.client.get(reverse('transaction:index'))
        self.assertEqual(response.status_code, 200)


Great job on completing the third part of this project! In this Task, we learned how to do a basic test for a view.

In the next Task, we’ll pick up where we left off here and we will create the Report view and learn how to test it.

Task 4: Test the report app view

Welcome back!

In the fourth task of this project, we will create the report app view and learn how to write tests for the view function.


First, we are going to create the view function:

def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'report/index.html', {'transactions': transactions})


Second, we will create the report index template:
<html>

<head>
    <title>POS</title>
</head>
<body>
    {% if transactions.count == 0 %}
    <p>No transactions yet.</p>
    {% else %}
    <ul>
        {% for t in transactions %}
        <li>{{t}}</li>
        {% endfor %}
    </ul>
    {% endif %}
</body>

</html>

Now, let us do the following two tests:
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



Great job on completing the fourth part of this project! In this Task, we created the report app view and learned how to test it.

In the next and last Task, we’ll pick up where we left off here and we will test the form in the transaction app, and then run the tests that we have written.

Task 5: Test the form

Welcome back!

In the fifth and last task of this project, we will learn how to test the form in the transaction app.


class TransactionFormTests(TestCase):
    def test_validation_do_not_accept_blanks(self):
        form = TransactionForm(data={})
        self.assertFalse(form.is_valid())


OK, now let’s run our tests!

python3 manage.py test transaction
python3 manage.py test report

Woops we have some issues in our code! Now let’s go and check them, and correct them!

I hope you’ve enjoyed our learning journey, and I wish you will find this learning useful to you. 

One last thing, I would appreciate that you provide your feedback and star rating to my project.

