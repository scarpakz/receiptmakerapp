from django.test import TestCase
from dashboard.models import ReceiptModel
from django.utils import timezone

class ReceiptModelTestCase(TestCase):
    """
    Create objects and check values
    """
    def setUp(self):
        ReceiptModel.objects.create(
            company="company",
            product="product",
            price=0.0,
            purchaser="purchaser",
            notes="",
            quantity=1,
            hst=0.15,
            total=0,
            date_added=timezone.now()
        )

    """
    Check object types by adding values to it.
    """
    def test_objects(self):
        company = ReceiptModel.objects.get(company="company")
        product = ReceiptModel.objects.get(product="product")
        price = ReceiptModel.objects.get(price=0.0)
        purchaser = ReceiptModel.objects.get(purchaser="purchaser")
        notes = ReceiptModel.objects.get(notes="")
        quantity = ReceiptModel.objects.get(quantity=1)
        hst = ReceiptModel.objects.get(hst=0.15)
        total = ReceiptModel.objects.get(total=0)

        self.assertEqual(company.company,"company")
        self.assertEqual(product.product,"product")
        self.assertEqual(price.price,0.0)
        self.assertEqual(purchaser.purchaser,"purchaser")
        self.assertEqual(notes.notes,"")
        self.assertEqual(quantity.quantity,1)
        self.assertEqual(hst.hst,0.15)
        self.assertEqual(total.total,0)