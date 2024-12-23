from django.db import models

class ReceiptModel(models.Model):
    company = models.CharField(max_length=250)
    product = models.CharField(max_length=250)
    price = models.FloatField(max_length=100)
    purchaser = models.CharField(max_length=250, default="")
    notes = models.TextField(default="")
    quantity = models.IntegerField()
    hst = models.FloatField(max_length=2, default=15)
    total = models.FloatField(max_length=100, default=0)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company