from django.db import models

class ReceiptModel(models.Model):
    company = models.CharField(max_length=250)
    product = models.CharField(max_length=250)
    price = models.FloatField(max_length=100)
    quantity = models.IntegerField()
    hst = models.FloatField(max_length=2)
    date_added = models.DateTimeField(auto_now=True)