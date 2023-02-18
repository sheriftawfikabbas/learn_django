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
