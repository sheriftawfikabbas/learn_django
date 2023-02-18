Build web apps with Django models, views, forms & templates

Task 1: Create a new Django project, its apps and setup the project

Welcome to this guided project about how to “Django models and views: create a bookstore web app.” 

My name is Sherif and I will be your instructor for this project. I am a research fellow in the field of computational material science and I do most of my programming in python. 

This project is for people who are interested in learning how to write advanced web applications using Django. 

I’ll teach you how to create database web applications in Django by using the object relational model. 

We will learn how several applications can share models, how to write Django templates and how to query model objects.

I would like to note that to get the most out of this project, you should have a basic understanding of the python and Django. Are you ready? Let’s get started!

I’m excited to teach you Django, and I hope that skills you will gain from this project will be useful for your web development tasks.

Let’s take a bird’s eye view at what you’ll accomplish by the end of this project. You will generate a new Django project, and create two applications in that project, a frontend and a backend application. In each of the front end and the back end apps, you will create a view and a HTML template, and you will create a model and a model form in the back end app. You will let the front end app use the model in the back end, and will examine the beauty of using model form objects to speed up the design of HTML forms.

Let’s dive right in. Once you load your cloud desktop, you’ll find the terminal app, the Google Chrome browser and Microsoft Visual Studio Code on the desktop. We will be using these apps throughout the project.

The first thing we will do in this task is to open the terminal and change directory to the Desktop:

cd Desktop

Then we will create a new Django project and two apps, frontend and backend:

django-admin startproject bookstoreproject
cd bookstoreproject
python3 manage.py startapp frontend
python3 manage.py startapp backend
code .

A Django project is composed of a number of apps. Each app comes with its own settings, views, models and urls. In the upcoming tasks we will be developing views and a model in the project apps. Here we will set up the urls in the project’s urls.py file.

First we import the include module

from django.urls import include
then we add the following two urls:

    path('display/', include('frontend.urls')),
    path('backend/', include('backend.urls')),

Then in the frontend and backend apps, we create a urls.py file. In the frontend app, we add the following text to urls.py:

from django.urls import path
import frontend.views as views

urlpatterns = [
   
]

And in the backend app’s urls.py, we add the following text:

from django.urls import path
import backend.views as views

urlpatterns = [
   
]

Great job on completing the first part of this project! In this Task, we learned about how to create a new Django project, its frontend and backend apps, and setup the URLs of the project.

In the next Task, we’ll pick up where we left off here and we will learn how to create the Book model, register it in the admin and let the two apps share it.

Task 2: Create the Book model, register it in the admin and let the two apps share it

Welcome back!

In the second task of this project, we are going to learn how to create the Book model, register it in the admin and let the two apps share it.

Remember: Djang is an object-relational mapping ORM platform, in which you can perform SQL operations using the language of object oriented programming. And you can create tables by creating classes which inherit the models.Model class in Django.

In Django models, you can define class variables, where each variable will correspond to a table field. Those variables must be defined as class, rather than instance, variables. So you cannot define your model attributes as variables inside the __init__() constructor of the model. Only class variables are allowed to be model attributes, and hence, table fields.

Just like table fields must have data types, such as integers, varchar, text and so on, Django has a large number of possible attribute types which we can use, and which will automatically correspond to the correct data type in the target database system that the model will be translated to. We are using the most basic database server here, which is the SQLite for simplicity, and whatever SQL that Django will generate for us, it will be compatible with SQLite.

Each data type in Django is represented as a subclass of the Field class, and the names of those classes go like SomethingField. For example, the integer type is handled by the class IntegerField, the char type is the class CharField, and so on.

So now let me keep explaining Django models in light of some code. Let’s type the following into the models.py in the backend app. It’s the model we will be using throughout this project.

from django.db import models

class Book(models.Model):
    FICTION = 'FI'
    NONFICTION = 'NF'
    SCIENCE = 'SC'

    BOOK_TYPES = [
        (FICTION, 'Fiction'),
        (NONFICTION, 'Non-fiction'),
        (SCIENCE, 'Science')
    ]

    book_title = models.CharField(max_length=200,unique=True,null=False)
    authors = models.CharField(max_length=200,null=False)
    book_type = models.CharField(
        max_length=2,
        choices=BOOK_TYPES,
        default=NONFICTION,null=False
    )
    price = models.FloatField(default=0,db_column='the_price',null=False)

    
    def to_string(self):
        return self.book_title+' by '+self.authors+', $'+str(self.price) + ' ('+self.book_type+')'


Let me explain what’s going on. This model has 4 attributes: book_title, authors, book_type and price. Both book_title and authors are CharField, like varchar in SQL, and price is a floating point number. However, book_type is different. Even though it’s a CharField like book_title, it has the “choices” attributed set to a list of tuples, the BOOK_TYPES tuple. This makes this field have one of a number of choices. 

Let me talk a bit more about choices field. You can set the choices for any type of field in Django. So for example, for a IntegerField, which accepts integers, you can set the choices to be, for example, the numbers 1, 2 and 3. 

The values of a choices field should be an iterable of tuples, such as a list of tuples as in the code here. Note that this choices feature does NOT enforce any validation on what you enter into the field; you can really enter anything there. What this feature does, though, is that it places those choices into the select HTML component on the Django form, as we will see in Task 6.

We can also have a quick look at how choices let us use a dropdown list by using the admin app. Let’s first register this model in admin.py:

from .models import Book

admin.site.register(Book)

and create the admin superuser:

python3 manage.py createsuperuser

Now this is what we get when we want add a new Book record. Note the dropdown menu, which was automatically provided because we have made the book_type record a choices field.

 

Now, back to the model. I have also set a few more Field options, apart from choices, so that we learn more about how the Field class works. I have set the null, unique and db_column options. If you set null to True, it will accept nulls for the respective field. It is False by default. If you set unique to True, it will only accept unique values for the respective field. So, I don’t want to see any duplicate book titles in the bookstore, so that’s why I set unique to True here. This might not be a typical scenario, but I did it here just for demonstration. And finally, the db_column just sets the database table column to a specific name; by default, Django will use the python attribute name to be the table column name.

Note that we haven’t explicitly created a primary key field here. Django will created it for us. However, if you want to have some control over this field, you can create it yourself by using the AutoField data type.

Finally, let’s register our two apps, to finish off the app creation. This is by adding those two lines into the settings.py file in the INSTALLED_APPS list:
    'backend.apps.BackendConfig',
    'frontend.apps.FrontendConfig',

And that’s it for this task!

Great job on completing the second part of this project! In this Task, we learned about how to create the Book model, register it in the admin and let the two apps share it.

In the next Task, we’ll pick up where we left off here and we will learn how to create the frontend view function and re-use the backend Book model class.

Task 3: Create the frontend view function and re-use the backend Book model class

Welcome back!

In the third task of this project, we will we will create the frontend view function and re-use the backend Book model class.

Let me briefly introduce how Django manages the user interface. When the user enters a URL into the address bar of the web browser, Django receives this request as a HTTP request, and processes the URL by checking the list of URL in the urls.py inside the project (not inside the app, yet). Recall that, what we have done in Task 1 is that we have made the project urls.py file [points by mouse] direct Django to the urlpatterns list sitting in the urls.py files inside the apps of the project.

Once Django goes to the right path inside the urlpatterns list, it will call a view function. This view function will render HTML into the web browser. So, the view manages what the user sees eventually.

Here we are going to create a basic view for the frontend app. Let’s type the following code.

from django.http import HttpResponse
from django.shortcuts import render

from backend.models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'frontend/display.html', {'books': books})


The index function retrieves all books using the objects.all() function, and then passes the set of books into a HTML file, the Django template.

Let me talk about the render function in detail. 

Instead of using the HttpResponse object to render text straight into the browser, we are using the render function which enables us to render the html text from a separate html file, called the template. 

Django templates are a mechanism to separate the view logic from the actual HTML, which is very useful design pattern and is utilized in other MVC, or model-view-component frameworks, such as Java’s SpringMVC. 

The template lets the web development team split the design of the interface into separate concerns: the view logic, where Django processes GET or POST parameters, perform database functions and what not, and the HTML file. 

As we will see in the next Task, Django templates let you add special tags within the HTML text to retrieve parameter values, perform if statements and for loops as well as other features. 

What’s cool about the template tags is that you can still browse the template HTML file on its own, without having to have Django server running at the backend. 

This enables the frontend web designer to have a workable “template” to design, rather than having a server page which won’t work outside of the server.

Another important detail in this file is the model we are using. Note that we have imported the Book model from the backend app. 

So, we did not have to create a new Book model in the frontend app! 

This is one of the nice features of ORM in Django: objects can be reusable throughout the project. And if you think about it, it would be pointless to have two Book tables in the database anyway.

Now, to make this view work, we need to add this line into the urls.py of the app:

path('', views.index),

It won’t work yet though, until we create the template, which is what we will do in the next Task.

Great job on completing the third part of this project! In this Task, we created the frontend view function.

In the next Task, we’ll pick up where we left off here and we will learn how to create the frontend view template.

Task 4: Create the frontend view template

Welcome back!

In the fourth task of this project, we will create the frontend view template, which I have introduced in the previous task.

We create templates into a templates folder, which we have to create inside the app. So let’s create this folder. The folder structure will now look like this:

 

Note that we have to create templates, then frontend inside templates, then our template file, display.html inside frontend. We don’t put display.html right inside the templates folder, because that’s how Django works. 

Next, we type the following into the display.html file.

<html>

<head>
    <title>Bookstore</title>
</head>

<body>
    <h1>Books</h1>
    <ul>
        {% for book in books %}
        <li>{{book.to_string}}</li>
        {% endfor %}
    </ul>
</body>

</html>

You can see that it’s mostly a standard HTML file with all the basic HTML tags. The only bit that looks different are the {% %} and {{ }} brackets. Those are the special Django template tags that empower Django templates to perform tasks on the variables that the template receives from the server.

The variable that this template has received is the “books” variable, which is a collection of Book objects. They were passed into the template via the render() function in the index view function, which we created in the previous Task. 

There are two main types of tags in Django:

{% %} are for instructions, which basically let the template perform programmatic tasks such as if statements and for loops. The code we wrote here shows the most simple syntax for a for loop in the Django template, which is very similar to the syntax of the for loop in python. However, whenever we open a for loop in the template, we have to close it with the {% endfor %} tag.

{{ v }} is to display the value of an expression. An example is in the code we wrote, which displays the value in the book.to_string. It calls the to_string method in the Book class, and then renders its output as text.

We are now ready to browse our frontend view. First, let’s enter some Book data into the admin view. First, let’s migrate the apps:

python3 manage.py makemigrations backend
python3 manage.py sqlmigrate backend 0001
python3 manage.py migrate

Note that we won’t need to migrate the frontend app, since that we didn’t create a model there. 

Now, let’s start the engine and go to the admin page to create a new book.

python3 manage.py runserver


 
Click ‘+’ next to Books:


 
Then we fill in some data.

 

Then click Save.

Next, browse to http://localhost:8000/display/

 

That’s awesome! So now we know that everything we’ve been building so far is error-proof, and we are ready for the next tasks.

Great job on completing the third part of this project! In this Task, we created the frontend view template.

In the next Task, we’ll pick up where we left off here and we will learn how to create the backend view function and the BookForm class.

Task 5: Create the backend view function and the BookForm class

Welcome back!

In the fifth task of this project, we will create the backend view function and the BookForm class.

The backend is where we will enter new Books into the database. We will need to create two view functions here: an index function that displays the form template, and a save function which will be called by the form to save data.

Let’s type the following code into the views.py file of the backend app:

from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

def index(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request,'backend/index.html',{'form': form})

The index() function here doesn’t look much like the index() function of the frontend app, so let me explain it slowly.

First we have the BookForm object. What’s that doing here?

In Django, you can create a ModelForm object for every Model you create. ModelForm objects are extremely useful, because they can very rapidly render your form for you as HTML, without you having to write the HTML for the form field. Say you have a Model that has 20 fields and you need to create a form to fill them up. That would be a daunting task. However, Django can do all the hard work for you if you create a ModelForm for that Model!

We will create a BookForm class that inherits the ModelForm class. For that, let’s create a new python file, call it forms.py, inside the backend app. Then type this into it:

from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
         model = Book
         fields = '__all__'

So what we’ve done here is that we are using all fields from the Book model as form fields. That’s what the line fields = '__all__' means here.

Now I will go back and continue explaining the index() view function. What this function does, in a nutshell, is the following: first, it checks if the view was requested as a POST request. If so, it checks if the form data is valid. If so, it saves the data in the form into the database using the ModelForm save() function. If no POST request was made, it just renders the form.

Let’s see how these steps are performed in code. The following two lines will check if the request is a POST request, and if so, will create a new form object.

if request.method == "POST":
        form = BookForm(request.POST)

Then, these lines will check if the form data are valid, and if so, save the form into the database.

if form.is_valid():
            form.save()

Otherwise, if someone visited the form without requesting to submit it, just present the form fields, using those two lines of code.

else:
        form = BookForm()

Finally, render the form.

return render(request,'backend/index.html',{'form': form})

Let’s now add the URL to the index() function in urls.py in the backend app.

path('', views.index,name='index')

Note the name attribute – we are going to need it in the template that we will create in the next Task.

And that’s all for now!

Great job on completing the fourth part of this project! In this Task, we learned about how to create the backend view function and the BookForm class.

In the next Task, we’ll pick up where we left off here and we will learn how to create the backend view template.

Task 6: Create the backend view template and demo the project

Welcome back!

In the sixth and last task of this project, we will create the backend view template and demo the project.

Let’s type the following code into views.py:

<html>

<head>
    <title>Backend</title>
</head>

<body>
    <form action="{% url 'index' %}" method="post">
        {% csrf_token %} {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
</body>

</html>

In this template, we are meeting with a few new things we haven’t seen in the frontend template. Let me take them one by one.

First, the action HTML attribute. We are using the {% %} again here to retrieve the URL of the index view function. This is a special syntax in Django forms, where you can specify the URL by using the string name corresponding to the path. Recall that, when we wrote the URL for the backend index, we specified a name [displays the code]. The purpose of name here is to use it in places like this, between the {% and %} brackets in the form.

Next, you can notice the {% csrf_token %} tag. I won’t spend much time on it, but will only say that it stands for Cross Site Request Forgery protection, and it is a must in Django forms for security reasons.

Next, is the forms magic: {{ form.as_p }}. This tag renders the form HTML entirely here, so we don’t have to worry about creating new text fields, drop down boxes, and so on. Specifically, if you write {{ form }}, you will get the whole form but all fields next to each other. The “as_p” renders each field with a <p> tag.

Let’s have a look at the backend form. Go to the browser and type

http://localhost:8000/backend/

And here is what we will get.

 
Fantastic! So now we can see the form working. Let’s remove “as_p” and see what we get.

 
It doesn’t look very pretty. It’s because we removed the <p> tags from HTML. I will put as_p back.

OK, now let’s test the form and enter some data.

 

Then click Save. Next, visit the display page on the browser.

 
Terrific! So the two books we entered are now appearing here on the display page. This completes our project!

Great job on completing the sixth part of this project! In this Task, we learned about how to create the backend view template and demo the project.

And I hope you have enjoyed our journey in developing web apps using python and Django.

