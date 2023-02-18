Objectives:
Understand how to efficiently preload data for testing in Django
Understand how to customize project settings during a test
Understand how the examine the HTTPResponse object in detail
Understand how to skip tests
Tasks:
Understand the sample project and install Beautiful Soup
Navigate the sample project and setup the test data using fixtures
Override your Django project settings during the test
Test form submission
Test the HTTPResponse object for containing strings
Perform tests on HTML strings using Beautiful Soup
Let some of your code skip tests

Apply advanced testing for your Django web application

Task 1: Understand the sample project and install beautiful soup
•	Welcome to this guided project about how to “Apply advanced testing for your Django web application.” 
•	My name is Sherif and I will be your instructor for this project. 
•	I am a research fellow in the field of computational physics and I do most of my scientific and business programming in python.
•	This project is for people who are interested in learning the advanced details Django web app testing.

•	Before I start, I would like to note that to get the most out of this project, you should have at least 1 year of experience with Django development. 
•	Are you ready? Let’s get started!


•	I’m excited to teach you advanced testing in Django, and I hope that skills you will gain from this project will be useful for your quality assurance tasks.

•	Let’s take a bird’s eye view at what you’ll accomplish by the end of this project. 
•	You will understand a basic Django project that contains two Django apps. Each app has a view
•	After that, we will perform various text exercises on the view of each app.


•	Now, let’s dive right in. 
•	Once you load your cloud desktop, you’ll find the terminal app, the Google Chrome browser and Microsoft Visual Studio Code on the desktop. We will be using these apps throughout the project.


cd Desktop
cd pos
code .

in order to launch Visual Studio code and open the files of the pos project for editing.

The file structure in visual studio code looks like this:

Now let’s migrate and run it:
python3 manage.py migrate
python3 manage.py runserver

Here is how it works: transaction/report
Install beautiful soup:
pip3 install bs4
We are now ready to start testing our project, which we will be doing in our next task!
Great job on completing the first part of this project! In this Task, we navigated the sample Django project and understood how it works.
In the next Task, we’ll pick up where we left off here and we will learn how to setup the test data using fixtures.

Task 2: Navigate the sample project and setup the test data using fixtures

Welcome back!
•	In the second task of this project, we are going to learn how to use fixtures for Django testing.
•	A fixture enables your Django test class to import test data from a file, rather than having to do that in code.
•	The fixtures variable exists in TestCase, and is a list of file names. Those files are the data files that contain the data.
•	Django supports json and yaml data formats, and we will stick to json here.
•	We setup the fixture by creating a new folder, fixtures.
•	Next, we add this json file.
•	Then, we add the fixtures variable to the test class

Task 3: Override your Django project settings during the test
Welcome back!
In the third task of this project, we will learn how to Override your Django project settings during the test.
First, why would we need to do that? Let’s have a look at settings.py file:
•	These are the global project settings that will applied when the server runs. 
•	Sometimes you would want to test whether a change in the settings will lead to errors, or you just want the test settings to be different from that of the app.
In this task, we will place a dummy variable, TRANSACTION_URL, and change its value within a test.
We will do that in such a way that: the test function will change the value, then the value will go back to normal after the test.
We will learn two ways to do that:
1.	The “with” clause
2.	The @override_settings decorator

Well done on completing the third task of this project. We learned how our test function can change a setting in the settings.py file.
In the next Task, we’ll pick up where we left off here and we will learn how to test form submission.

Task 4: Test form submission
Welcome back!
In the fourth task of this project we are going to learn how to test form submission in Django.
Each TestCase class comes with a Client object. We submit a form by using the post or the get function in the client object.
 def test_invalid_form_submission(self):
        response = self.client.post(
            "/transaction/", data={}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Transaction.objects.all()), 2)

Well done on completing the fourth task of this project. We learned how our test form submission using the post method in the client object.
In the next Task, we’ll pick up where we left off here and we will learn how to test response object for containing strings.

Task 5: Test the HTTPResponse object for containing strings
Welcome back!
In the fifth task of this project, we will learn how to check the HTTPResponse object for including strings. We will be using the assertContains method of the TestCase class.

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

Well done on completing the fifth task of this project. We learned how our test the HTTPResponse object for containing strings.
In the next Task, we’ll pick up where we left off here and we will learn how to test HTML strings.

Task 6: Perform tests on HTML strings using Beautiful Soup
Welcome back!
In the sixth task of this project, we will learn how to use some of the assert methods that are concerned with HTML strings. We will augment our tests by using Beautiful Soup. 
Beautiful Soup is a python library that helps in parsing HTML strings. You create a Beautiful Soup object based on some HTML text, and Beautiful Soup will go through the string and discovers all the tags, attributes, contents and maps the organization of the HTML into Tag objects.
Let’s see how this goes in code. 
First we use the assertHTMLEqual method. It enables us to do comparisons between HTML tags, without having to worry about the exact number of spaces or order of attributes within a tag. Let’s see and example below.
# Task 6
    def test_html(self):
        response = self.client.get(reverse('report:index'))
        soup = BeautifulSoup(str(response.content))
        li = soup.find_all('li')[0]
        self.assertHTMLEqual(str(li), '<li>Laptop_2_1000.0</li>')
        self.assertInHTML('<li>Laptop_2_1000.0</li>', str(response.content))

For bs4, we will use the find_all method and specify the li tag, because we want the list of transactions in the report.
Well done on completing the sixth task of this project. We learned how our test perform tests of HTML strings using the assert HTML methods and bs4.
In the next Task, we’ll pick up where we left off here and we will learn how to instruct Django to skip tests.

Task 7: Skip tests
Welcome back!
In the seventh and last task of this project, we will learn how to instruct Django to skip tests.
Sometimes you would create a test which, later, you don’t want to use. So you can ask Django to skip it using either the @unittest.skip() decorator or the skipTest method. Let’s see an example.

 # Task 7
    @unittest.skip("This will be skipped")
    def test_skipping(self):
        self.assertEqual("This test must be skipped", "This test should be skipped")
    
    def test_skipping_within(self):
        self.skipTest("Will skip this test too")
        self.assertEqual("This test must be skipped", "This test should be skipped")
        

Well done on completing the last task of this project, where we learned how to instruct Django to skip tests.
I hope you’ve enjoyed our learning journey, and I wish you will find this learning useful to you. 
One last thing, I would appreciate that you provide your feedback and star rating to my project.




