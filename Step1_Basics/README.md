Creating a simple contacts list app using django

Task 1: Create a new Django project

Welcome to this guided project about how to “Creating a simple contacts list app using Django.” My name is Sherif and I will be your instructor for this project. I am a research fellow in the field of computational science and I do most of my programming in python. This project is for people who are interested in learning how to write web applications in the python programming language. I’ll teach you how to create database web applications in Django by using the object relational model in Django. I would like to note that to get the most out of this project, you should have a basic understanding of the python programming language. Are you ready? Let’s get started!

I’m excited to teach you Django, and I hope that skills you will gain from this project will be useful for your web development tasks.

Let’s take a bird’s eye view at what you’ll accomplish by the end of this project. You will generate a new Django project, and create a contacts list application in that project. You will learn how Django separates between the model and the view in a web application. You will learn how the model translates into an SQL database, and will be able to see the database table and data via Django’s admin app, as well as by accessing the database directly. Finally, you will create a view that displays the contacts that are saved in your database on the web browser.

Let’s dive right in. Once you load your cloud desktop, you’ll find the terminal app, the Google Chrome browser, Microsoft Visual Studio Code and the DB Browser for SQLite on the desktop. We will be using these apps throughout the project.

The first thing we will do in this task is to open the terminal and change directory to the Desktop:

cd Desktop

Then we will create a new Django project using the installed django-admin program:

django-admin startproject contactsproject

Note that we should avoid naming projects after built-in Python or Django components.

Let’s have a look at the project’s file structure in Visual Studio code. To do so, we will change directory to our project:

cd contactsproject

and then we will type 

code .

in order to launch Visual Studio code and open the files of the contactsproject for editing.

The file structure in visual studio code looks like this:


 


Let’s have a quick overview of these files:
•	The contactsproject/ root directory is a container for your project. You can assign it any name you want.
•	manage.py: the manager utility of Django that lets you control Django in several ways, as will see throughout this project.
•	settings.py: configurations of your project.
•	urls.py: the settings that map browser URLs to views in the project.
•	asgi.py and wsgi: for production deployment. We will not be working with those in this project.

Now that we have created a project, guess what? Django can let us make this project go live pretty easily!

python manage.py runserver

You can notice these warning messages here, which complain from some “unapplied database migrations”. Ignore those for now, we will deal with this in task 4.

We can now take a look at our live project on the web browser. Open the web browser and type this web address, then enter!

localhost:8000

 

What we see here is Django celebrating your first Django web project!

Now you notice that the default port that Django uses is port 8000. We can actually choose a different port by typing it after the runserver command. Let’s say you want to use the 8765 port?

python manage.py runserver 8765

To see if it is working, type this in the web browser:

localhost:8765

And here you go!

Great job on completing the first part of this project! In this Task, we learned about how to create a new Django project, run the project in Django’s development server and view the default project page on the web browser.

In the next Task, we’ll pick up where we left off here and we will learn how to create a new app in your project.

Task 2: Create the app and your first view

Welcome back!

In the second task of this project, we are going to learn how to create a new application in the project we created in task 1. But before I dive deeper here, let me first explain the difference between an app and a project.

A project is a collection of settings and apps for a particular website. Let’s take the example of an ecommerce website. A few features of this website would be: product display page, shopping cart, online payment page, and so on. Each one of those features, or let’s say functions, represent an app within the website. 

So while the whole website is a Django project, a function such as the shopping cart is a Django app within the website.

So, a project can contain multiple apps. An app can be in multiple projects, but this will be outside of the scope of this guided project.

To create an app into our new project, we type:

python manage.py startapp contactslist

This will create for us the following set of new files:

contactslist/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

Let me give you a quick overview of these files.
    __init__.py: This is again a constructor file for the module
    admin.py: The admin module which we will deal with in task 5
    apps.py: This configuration class for our app
    migrations: Whenever we make edits to our database model, such changes will be recorded in the migrations folder.
    models.py: That’s where we will create our new database objects, tables.
    tests.py: That’s for performing automated tests of our new app. It’s outside the scope of this project.
    views.py: That’s where we will write the user interface for our app.

The new app contactslist should become accessible through the web browser, but not yet. We will need to learn how to create a view, and setup the urls.py python file, and this is what we will do in the next session.

Great job on completing the second part of this project! In this task, we learned about how to create a new app in the project we created.

In the next Task, we’ll pick up where we left off here and we will understand the model-view concept in Django, create a new view and map the view to a URL.

Task 3: Views

Welcome back!

In the third task of this project, we will we will understand the model-view concept in Django, create a new view and map the view to a URL.

When designing a backend for your web application, a reasonable thing to do is to separate the code that deals with the front end from the code that deals with the data. This separation is known as the model-view-controller software design patter, where the view controls the frontend, the model controls the data, and the controller manages the input and output of the web application.

A view in Django is the interface that you will provide to your users. We write our views as python functions in the view.py file. Let’s have a look at this file.

By default, the file is already there in the new contactslist app. Let’s add the following code to it:

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello!")


In this code we are creating a new view for the app, and this is done by creating a python function, we call it index(), and passing the request argument to it. This function returns a HttpResponse object to the requester; the requester here being the web browser. The argument of this HttpResponse object is just the text we will see in the browser when we request this view.

However, we are not done yet! We still need to map this python function to a URL. This can be done in the url.py file by applying those two changes:

First, we add this import:

from contactslist import views

and then add this line inside the urlpatterns list:

path('contactslist/', views.index, name='index')

Now, let’s have a look at the app in the browser by typing 

localhost:8000/contactslist/

And we get the “Hello!” message in the browser! 

Great job on completing the third part of this project! In this Task, we understood the model-view concept in Django, created a new view and map the view to a URL.

In the next Task, we’ll pick up where we left off here and we will learn how to create a new Django model, migrate the project and access the generated SQLite database using a third party software.

Task 4: Create Django models

Welcome back!

In the fourth task of this project, we will learn how to create a new Django model, migrate the project and access the generated SQLite database using a third party software.

In this task we learn how to create a model in Django. A model represents a table in a database. Representing databases entities as model objects is a paradigm in database development known as object relational model (ORM), and Django is an example ORM platform. In ORM platforms, you create the database as a set of object, instead of creating it as a set of tables in a database management system such as MySQL or Microsoft SQL server.

In Django, the model is a python class which inherits the Model class in the models module in Django.


Let us write our first model: the Contact model. We will write the Contact class into the models.py file.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField() 

This model has 4 attributes: the first_name, last_name, email and comment. Each attribute here is initialized with a model field object. The model field object define the type of the attribute. 

CharField is a character field, and max_length states the maximum number of characters in the attribute. TextField is a another character field which can hold large text data.

Too demonstrate the correspondence between the database table and the Django model here: the Contact model corresponds to a database table called Contact, which has four columns: first_name, last_name, email and comment. Each column in the table has a data type. I will show you shortly that Django does indeed translate the Contact model into a create statement for a database table!

To get ready to setup the model we just wrote, we have to add the configuration class of our app to the list of INSTALLED_APPS in the settings.py file. We do this by adding this item to the list:

'contactslist.apps.ContactslistConfig',

Note that the ContactslistConfig actually does exist in the apps.py file of the contactslist app.

So what we just did was completing the setup of the entire app into the project.

Now we are ready to setup our model. Type the following into the terminal:

python3 manage.py makemigrations contactslist

And you will get the “Create model Contact” line in the output.

Next, type the following: 

python3 manage.py sqlmigrate contactslist 0001

And then notice the output in the terminal. You can clearly see now that the model we are setting up is translating it a database SQL create statemen:

BEGIN;
--
-- Create model Contact
--
CREATE TABLE "contactslist_contact" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(200) NOT NULL, "last_name" varchar(200) NOT NULL, "email" varchar(200) NOT NULL, "comment" text NOT NULL, "contact_type" varchar(2) NOT NULL);
COMMIT;

Finally, type the following:

python3 manage.py migrate

The migrate command implements all new migrations you have against your database. Each such migration is a change you made to the models but has not been reflected into the actual database.

Let’s have a look at the database we have just created using the DB Browser for SQLite, which is a free open-source and widely used software for browsing SQLite database files.

 
Here we can see the translation of the Contact model class into a database table, named contactslist_contact in the SQLite database file. The CharField objects translated to varchar(200) table fields, and Django added the id primary key field automatically to the table.

Great job on completing the fourth part of this project! In this Task, we learned about how to create a new Django model, migrate the project and access the generated SQLite database using a third party software

In the next Task, we’ll pick up where we left off here and we will learn how to register your model in the admin app, access the model in the admin interface and enter data directly into the model.

Task 5: Django admin

Welcome back!

In the fifth task of this project, we will learn how to register your model in the admin app, access the model in the admin interface and enter data directly into the model.

Django comes with a nice database administration app, called the admin. It lets you inspect and edit your database.

In this task we are going to learn how to access the admin app. To do so, we need to do two things.

First, we create an admin account:

python3 manage.py createsuperuser

This will prompt you to enter your username, email address and password. Once you are done, you can access the admin page by going to the address localhost:8000/admin

 

Now enter the username/password, and you will get the admin page:

 
This displays the user admin controls: groups of users, and individual users. However, we are not yet seeing our Contact model here. This is because there is one more step that needs to be done in the admin module: we need to register our model!

To do so, go to admin.py and type

from .models import Contact

admin.site.register(Contact)

Then let’s refresh the admin page.

 
Now we can see the Contacts object.

Let’s add two new contacts to our database. We can do this easily using the admin interface. Just click on the Add button next to “Contacts” on the admin page.
 

Let’s add two contacts in this interface. After we are done, we will see the two contact objects created on the admin interface.

 

On the database side of things, let’s have a look at the SQLite database.

 

Great job on completing the fifth part of this project! In this Task, we learned about how register your model in the admin app, access the model in the admin interface and enter data directly into the model.

In the next Task, we’ll pick up where we left off here and we will learn how to create a view that queries all the data stored in the database and displays the data on the web browser.

Task 6: Contacts display view

Welcome back!

In the sixth and last task of this project, we will learn how to create a view that queries all the data stored in the database and displays the data on the web browser.

In this task, we will write a view that displays the contents of our Contacts model. We will add the following code to our app’s views.py file.

def display(request):
    contacts = Contact.objects.all()

    s=""
    for c in contacts:
        s+=c.to_string()+'<br>'
    return HttpResponse("Contacts:<br>"+s)

This python function will extract all the objects stored in the Contact model (via the objects.all() method of the Contact model), iterate through them and prints out each Contact object.

And we also need to add the “to_string()” method to the Contact model, because we are calling it in the display view function that we just added:

    def to_string(self):
        return self.first_name+' '+self.last_name+', '+self.comment

Next, we should link this function to a URL in the urls.py file, as we did with the index URL. To do so, we will add this line to urls.py:

path('display/', views.display, name='display'),



Now let’s have a look at the new display view by visiting

localhost:8000/display

And voila!


 
Great job on completing the sixth and last part of this project! In this Task, we learned about how to create a view that queries all the data stored in the database and displays the data on the web browser.

And I hope you have enjoyed our journey in exploring time series analysis using python.

