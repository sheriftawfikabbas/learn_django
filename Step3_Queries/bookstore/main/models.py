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
