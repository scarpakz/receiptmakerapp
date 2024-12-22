from django.db import models

class ReceiptModel(models.Model):
    company = models.CharField(max_length=250)
    product = models.CharField(max_length=250)
    price = models.FloatField(max_length=100)
    quantity = models.IntegerField()
    hst = models.FloatField(max_length=2)
    total = models.FloatField(max_length=100, default=0)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

    def calculate_total_price_without_tax(self):
        return self.price * self.quantity

    def calculate_tax(self):
        return self.calculate_total_price_without_tax() * (self.hst/100.0)

    def calculate_total_price_with_tax(self):
        return self.calculate_total_price_without_tax() * self.calculate_tax()