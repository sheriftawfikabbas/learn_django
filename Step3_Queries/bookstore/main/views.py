from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Book, Author, Publisher

# Task 2


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

    b3 = Book.objects.create(title='Machine learning',
                             price=110,
                             field='Data Science',
                             publication_date='2019-03-05', publisher=p3)
    b3.authors.add(a1, a3)

    return HttpResponse('Setup done!')


def index(request):
    # Task 2

    # Two categories of queries: keyword arguments and Q
    # all()
    results = Book.objects.all()

    # Task 3

    # QuerySet methods: they run queries and return a set of objects, which we can then iterate through

    # get() expects a keyword argument, it only returns a single object

    # Most basic keyword argument: field__lookuptype=value
    results = Book.objects.get(id=1)
    # pk is the same as id
    results = Book.objects.get(pk=1)
    # we can apply an operation to a keyword argument using the double underscore. Our first operation is exact
    results = Book.objects.get(id__exact=1)

    # Task 4

    # filter runs a query and returns multiple objects
    # Here we will learn field lookups: isnull, gt, gte, lt, lte, and date field lookups: year, month, day

    # filter: isnull
    results = Book.objects.filter(field__isnull=True)

    # filter: comparison
    results = Book.objects.filter(id__gt=1)
    results = Book.objects.filter(id__lte=4)
    results = Book.objects.filter(publication_date__gte='2000-01-01')
    results = Book.objects.filter(publication_date__year=2000)
    results = Book.objects.filter(publication_date__month__lt=6)

    # Task 5

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

    # Task 6

    # exclude
    results = Book.objects.exclude(field__isnull=True)
    # same as
    results = Book.objects.filter(field__isnull=False)
    results = Author.objects.exclude(name__contains="a")

    # filter: nesting
    # Order: left to right
    results = Book.objects.filter(id__gte=1).filter(id__lt=4)
    results = Book.objects.filter(
        price__gte=100).filter(price__lte=200)
    # Multiple keyword parameters
    results = Book.objects.filter(price__gte=100, price__lte=200)
    results = Book.objects.filter(price__lte=200).exclude(title__contains="j")

    # Task 7

    # Q objects
    q = Q(id=1)
    results = Book.objects.get(q)
    results = Book.objects.filter(Q(price__gte=100))
    results = Book.objects.filter(Q(price__gte=100) & Q(price__lte=200))
    results = Book.objects.filter(
        Q(title__contains="python") | Q(price__lte=200))
    results = Book.objects.filter(
        (Q(title__startswith="P") | Q(title__startswith="D")) & Q(price__gt=200))

    # Task 8

    # Queries across relationships
    results = Book.objects.filter(authors__name='Abdus Salam')
    results = Book.objects.filter(publisher__name__icontains='fantastic')
    results = Author.objects.filter(books__title__icontains='django')
    results = Author.objects.filter(
        books__publisher__name__icontains='fantastic')


    return render(request, 'main/index.html', {'results': results})
