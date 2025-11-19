from django.http import HttpResponse
from .models import Contact


def index(request):
    return HttpResponse("a")


def display(request):
    contacts = Contact.objects.all()

    s = ""
    for c in contacts:
        s += c.first_name + "<br>"
    return HttpResponse("Contacts:<br>" + s)
