from django.http.request import RAISE_ERROR
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import ReceiptModel

def index(request):
    return render(request, 'dashboard/index.html')

def create_pdf(request):
    return None

def create_receipt_view(request):
    HST = 15
    if request.method == "POST":
        company = request.POST.get('company')
        purchaser = request.POST.get('purchaser')
        product = request.POST.get('product')
        price =int(request.POST.get('price'))
        quantity = int(request.POST.get('quantity'))
        hst = HST
        notes = request.POST.get('notes')

        def calculate_total_price_without_tax():
            return price * quantity

        def calculate_tax():
            return calculate_total_price_without_tax() * (hst / 100.0)

        def calculate_total_price_with_tax():
            return calculate_total_price_without_tax() + calculate_tax()

        total = calculate_total_price_with_tax()

        receipt = ReceiptModel.objects.create(
            company=company,
            purchaser=purchaser,
            product=product,
            price=price,
            quantity=quantity,
            hst=hst,
            notes=notes,
            total=total
        )

    return render(request, 'dashboard/index.html')