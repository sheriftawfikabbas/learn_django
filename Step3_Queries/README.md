# Query data in Django web applications


## Objectives
- Learn how to query Django models using QuerySet methods and Q objects
- Learn how to construct complex queries
- Learn how to query across relationships

## Tasks

### Task 1: Create the bookstore Django project and its apps

We will generate a new Django project, and setup a view that will insert sample data for our queries. We will perform these steps in Tasks 1 and 2 of this project.

Then from tasks 3 to 8, we will write a new view in which we will demonstrate the two query systems supported by Django, namely using QuerySet methods and using Q objects.

'''
cd Desktop
django-admin startproject bookstore
cd pos
python3 manage.py startapp main
code .
'''

in order to launch Visual Studio code and open the files of the project for editing.

The file structure in visual studio code looks like this:


Now that we have created a project, let’s run it:

python manage.py runserver

Next, we will create the following in our project:
•	Setup the URLs
•	Create our 3 models
•	Create blank views: setup and index

from django.db import models
import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    authors = models.ManyToManyField(Author, related_name="books")
    field = models.CharField(max_length=100, null=True)
    publication_date = models.DateField(default=datetime.date.today())
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title



We are now ready to start entering data into our models, which we will be doing in our next task!

Great job on completing the first part of this project! In this Task, we created a basic Django project, sat up the URLs and created the model and blank views.

In the next Task, we’ll pick up where we left off here and we will learn how to test our model.

Task 2: Create the setup view which will automate entry of sample data

Welcome back!

In the second task of this project, we are going to learn how to programmatically enter data into Django.

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Book, Author, Publisher

def setup(request):
    a1 = Author.objects.create(name='Curie')
    a2 = Author.objects.create(name='Ramanujan')
    a3 = Author.objects.create(name='Abdus Salam')
    a4 = Author.objects.create(name='Einstein')

    p1 = Publisher.objects.create(name='Lebanon Publishing House')
    p2 = Publisher.objects.create(name='Fantastic Books')
    p3 = Publisher.objects.create(name='Scibooks')

    b1 = Book(title='Python programming',
              price=230,
              field='Computer Science',
              publication_date='2020-10-10', publisher=p1)
    b1.authors__set = a1
    b1.save()

    b2 = Book(title='Django security',
              price=110,
              field='Cybersecurity',
              publication_date='2019-03-05', publisher=p2)
    b2.save()
    b2.authors.add(a2, a3, a4)

    b3 = Book.objects.create(title='Django security',
                             price=110,
                             field='Cybersecurity',
                             publication_date='2019-03-05', publisher=p3)
    b3.authors.add(a1, a3)

    return HttpResponse('Setup done!')

We can use DB Browser to check the data in our tables.


Now to see the results of these data entry statements, let’s run a basic query using objects.all:


def index(request):
    results = Book.objects.all()



Task 3: Run queries using the QuerySet method get()

Welcome back!

In the third task of this project, we will start querying the bookstore database!

•	Django enables us to perform queries using two systems: the QuerySet methods, and the Q objects.
•	These systems enable us to query model objects from the database, and support adding conditions to our queries just like adding the where clause in SQL, and can enable us to perform queries across database relations, just like the SQL join clause.
•	We will start with learning the QuerySet methods. These methods include get(), filter() and exclude(). 
•	In a nutshell, 
o	get() will get a single object, 
o	filter() will retrieve a set of objects based on conditions, and 
o	exclude() gets a set of objects that do not satisfy a set of conditions; that is, it is opposite to filter().
•	So let’s start with get().
•	The get() method expect keyword arguments. A basic keyword argument has the form (in code)
•	The get() method will return only 1 object. If the keyword argument makes it to return none or more than 1, it will raise an exception.
•	That is why, the most common keyword argument of get() is based on the primary key: either id or pk.

 # Most basic keyword argument: field__lookuptype=value

    # get() expect an id, it only returns a single object
    results = Book.objects.get(id=1)
    # pk is the same as id
    results = Book.objects.get(pk=1)
    # we can apply an operation to a keyword argument using the double underscore. Our first operation is exact
    results = Book.objects.get(id__exact=1)

Great job on completing the third part of this project! In this Task, we learned how to do a run queries using one of the QuerySet set methods, namely get().

In the next Task, we’ll pick up where we left off here and we will learn how to query using the second QuerySet method, filter().

Task 4: Run queries using the QuerySet method filter()

Welcome back!

•	In the fourth task of this project, we will learn how to query using the second QuerySet method, filter().
•	It also expects keyword arguments like get(), but it is much more flexible. 
•	Here we will learn the following lookup types: isnull, gt, gte, lt, lte.
•	We will also learn how to extract year, month and day of a date field.
•	Importantly, you can see how the underscore is a big deal in Django, just like it is in Python.
•	Let’s have these examples.

# filter: isnull
    results = Book.objects.filter(field__isnull=True)

    # filter: comparison
    results = Book.objects.filter(id__gt=1)
    results = Book.objects.filter(id__lte=4)
    results = Book.objects.filter(publication_date__gte='2000-01-01')
    results = Book.objects.filter(publication_date__year=2000)
    results = Book.objects.filter(publication_date__month__lt=6)


Great job on completing the fourth part of this project! In this Task, we learned how to use the second QuerySet method filter().

In the next and last Task, we’ll pick up where we left off here and we will learn how to nest filters, how to use the in and string lookup types.

Task 5: Apply the membership and string lookup types.

Welcome back!

In the fifth task of this project, we will learn how to use the in and string lookup types.


    # filter nesting
    results = Book.objects.filter(id__gte=1).filter(id__lt=4)

    # filter: in
    results = Book.objects.filter(
        publication_date__year__in=[2000, 2002, 2005])

    # filter: exact, contains, startswith, endswith, iexact, icontains, istartswith, iendswith
    results = Book.objects.filter(title__exact='Python programming')
    results = Book.objects.filter(title__iexact='python programming')
    results = Book.objects.filter(title__startswith='Python')
    results = Book.objects.filter(title__endswith='security')
    results = Book.objects.filter(title__iendswith='secUritY')
    results = Book.objects.filter(title__contains='python')
    results = Book.objects.filter(title__icontains='pytHON')

And this concludes task 5 of the project!

Great job on completing task 6 of this project! In this Task, we learned how to use the in and string lookup types.

In the next and last Task, we’ll pick up where we left off here and we will learn how to use the third QuerySet method, exclude(), and how to nest filters.

Task 6: Query using the QuerySet exclude method and nest filters

Welcome back!

•	In the sixth task of this project, we will learn how to use the third QuerySet method, exclude(), and how to nest filters.
•	Let’s start with the exclude method.
•	Exclude is just the opposite of filter. For example, 

 results = Book.objects.exclude(field__isnull=True)
    # same as
    results = Book.objects.filter(field__isnull=False)
 results = Author.objects.exclude(name__contains="a")

•	Next up, let’s see how we can nest filters.
•	We can actually nest filter and exclude!

    # Order: left to right
    results = Book.objects.filter(id__gte=1).filter(id__lt=4)
    results = Book.objects.filter(
        price__gte=100).filter(price__lte=200)
    # Multiple keyword parameters
    results = Book.objects.filter(price__gte=100, price__lte=200)
    results = Book.objects.filter(price__lte=200).exclude(title__contains="j")


Great job on completing the fourth part of this project! In this Task, we learned how to use the second QuerySet method filter().

In the next and last Task, we’ll pick up where we left off here and we will learn how to nest filters, how to use the in and string lookup types.

Task 7: Query using Q objects

Welcome back!

•	In the seventh task of this project, we will learn how to use the Q objects in our queries.
•	Q objects enable you to combine several keyword lookups using the & and | logical operations.
•	Thus, they provide greater flexibility in constructing complex queries.
•	Lets see an example.


  q = Q(id=1)
    results = Book.objects.get(q)
    results = Book.objects.filter(Q(price__gte=100))
    results = Book.objects.filter(Q(price__gte=100) & Q(price__lte=200))
    results = Book.objects.filter(
        Q(title__contains="python") | Q(price__lte=200))
    results = Book.objects.filter(
    (Q(title__startswith="P") | Q(title__startswith="D")) & Q(price__gt=200))


Great job on completing the seventh part of this project! In this Task, we learned how to use the Q objects in our queries.

In the next Task, we’ll pick up where we left off here and we will learn how to run queries across relationships.

Task 8: Query across relationships

Welcome back!

•	In the 8th task of this project, we will learn how to run queries across relationships.

results = Book.objects.filter(authors__name='Abdus Salam')
    results = Book.objects.filter(publisher__name__icontains='fantastic')
    results = Author.objects.filter(books__title__icontains='django')
    results = Author.objects.filter(
        books__publisher__name__icontains='fantastic')



I hope you’ve enjoyed our learning journey, and I wish you will find this learning useful to you. 

One last thing, I would appreciate that you provide your feedback and star rating to my project.

