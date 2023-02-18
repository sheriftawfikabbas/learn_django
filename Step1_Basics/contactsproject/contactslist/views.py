from django.http import HttpResponse
from contactslist.models import Contact

def index(request):
    return HttpResponse("Hello!")

def display(request):
    contacts = Contact.objects.all()

    s=""
    for c in contacts:
        s+=c.to_string()+'<br>'
    return HttpResponse("Contacts:<br>"+s)
