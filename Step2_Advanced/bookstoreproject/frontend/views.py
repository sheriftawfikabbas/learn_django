from django.http import HttpResponse
from django.shortcuts import render

from backend.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'frontend/display.html', {'books': books})
