from django.db import models


class Transaction(models.Model):
    product_code = models.CharField(max_length=200, null=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
