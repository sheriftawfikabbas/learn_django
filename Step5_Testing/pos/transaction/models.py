from django.db import models


class Transaction(models.Model):
    product_code = models.CharField(max_length=200, null=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def price_is_valid(self):
        if self.price < 0:
            return False
        else:
            return True

    def apply_discount(self, discount):
        # self.price = self.price - self.price*discount/100
        self.price = self.price - self.price*discount

    def __str__(self):
        # return self.product_code+'_'+str(self.quantity)+'_'+str(self.price)
        return self.product_code+'_'+str(self.quantity)+str(self.price)
