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
