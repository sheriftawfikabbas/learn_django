from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Book, Author, Publisher, Country

# Task 1


def setup(request):
    c1 = Country.objects.create(name='Canada')
    c2 = Country.objects.create(name='Nigeria')
    c3 = Country.objects.create(name='Brazil')

    a1 = Author.objects.create(name='Omar Khayyam', country=c1)
    a2 = Author.objects.create(name='Al-Biruni', country=c1)
    a3 = Author.objects.create(name='Ibn Sina', country=c2)
    a4 = Author.objects.create(name='Al-Khwarizmi', country=c2)

    p1 = Publisher.objects.create(name='Lebanon Publishing House', country=c1)
    p2 = Publisher.objects.create(name='Fantastic Books', country=c3)
    p3 = Publisher.objects.create(name='Scibooks', country=c3)

    b1 = Book(title='Python programming', publisher=p1)
    # Must save before add, so b1 can get an "id"
    b1.save()
    b1.authors.add(a1)

    b2 = Book(title='Keras basics', publisher=p2)
    b2.save()
    b2.authors.add(a2, a3, a4)

    b3 = Book.objects.create(title='Machine learning', publisher=p3)
    b3.save()
    b3.authors.add(a1, a3)

    b4 = Book.objects.create(title='Mathematics', publisher=p3)
    b4.save()
    b4.authors.add(a2, a4)

    return HttpResponse('Setup done!')


def index(request):
    # Task 2: Perform deep lookups across multiple relationships

    # Get authors who published a book with "python" in the title
    results = Author.objects.filter(books__title__icontains="python")
    # Get counties of publishers with which authors
    # published books on Python.
    results = Country.objects.filter(
        publishers__book__title__icontains='python')
    # Get authors who published books with publishers in Canada
    results = Author.objects.filter(
        books__publisher__country__name__exact="Canada")

    # Task 3: Query with a filter inside a filter

    # The "in" field lookup tests membership
    # Simple example: get books published by ['Omar Khayyam','Ibn Sina']
    results = Book.objects.filter(
        authors__name__in=['Omar Khayyam', 'Ibn Sina'])

    # Now get books authored by people who reside in Nigeria.
    # For the purpose of exercise, let's see how to use a filter
    # inside a filter.
    results = Book.objects.filter(
        authors__in=Author.objects.filter(
            country__name__exact="Nigeria"
        )
    ).distinct()

    # Task 4: Apply nested filters and the comma across relationship

    # Get books published by authors who reside Canada,
    # the same country as the publishers. Use the comma.
    results = Author.objects.filter(
        country__name__exact="Canada", books__publisher__country__name__exact="Canada")

    # Same as above, but use nesting.
    results = Author.objects.filter(country__name__exact="Canada").filter(
        books__publisher__country__name__exact="Canada")

    # So here, nesting and comma play the same role:
    # an "and" operation.

    # Now the tricky filter queries:
    # We want publishers who published books with "Machine" in the title,
    # and authored by someone with "Biruni" in the name.
    # We know Biruni never authored on Machine learning!
    # So we get no results.
    results = Publisher.objects.filter(
        book__title__contains="Machine", book__authors__name__contains="Biruni")

    # Now let's use nesting. We get "Scibooks"! Why?
    # Let's analyse:
    # First filter: get all publishers that published on "Machine",
    # so we get Scibooks.
    # Second filter: out of the results of the first filter,
    # get publisher that published a book by Biruni.
    # Biruni did indeed publish with Scibooks, but
    # he published a different book.
    results = Publisher.objects.filter(book__title__contains="Machine").filter(
        book__authors__name__contains="Biruni")

    # Task 5: Apply exclude across relationships

    # It is stated on the Django documentation that:
    # "The behavior of filter() for queries that span
    # multi-value relationships ...
    # is not implemented equivalently for exclude()."

    # That is: what we learned in Task 5 for filters doesn't
    # apply for exclude. Let's see how.

    # Let's exclude publishers who published books
    # on "Machine" that are authored by "Biruni"
    results = Publisher.objects.exclude(
        book__title__contains="Machine", book__authors__name__contains="Biruni")

    # Comma here also acts as an "and" operator.
    # But we should only get 1 result: "Lebanon Publishing House"
    # However, we got 2 results! Why?

    # Reason: the "comma" in exclude does not refer to
    # the same database entry; both conditions are
    # applied on separate data.

    # To fix this, we must use a filter inside exclude!
    results = Publisher.objects.exclude(
        book__in=Book.objects.filter(
            title__contains="Machine", authors__name__contains="Biruni")
    )
   
    # Awesome! We get all 3 publishers because there is no such book.

    return render(request, 'main/index.html', {'results': results})
