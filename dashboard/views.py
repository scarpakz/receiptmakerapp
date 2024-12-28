from django.http.request import RAISE_ERROR
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import ReceiptModel
from fpdf import FPDF

def index(request):
    return render(request, 'dashboard/index.html')

def create_pdf(company, purchaser, product, price, quantity, hst, notes, total):
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # Add title
    pdf.cell(200, 10, company, ln=True, align='C')

    # Add receipt details
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)  # Line break
    pdf.cell(0, 10, f'Purchaser: {purchaser}', ln=True)
    pdf.cell(0, 10, f'Product: {product}', ln=True)
    pdf.cell(0, 10, f'Price: ${price:.2f}', ln=True)
    pdf.cell(0, 10, f'Quantity: {quantity}', ln=True)
    pdf.cell(0, 10, f'Subtotal: ${price * quantity:.2f}', ln=True)
    pdf.cell(0, 10, f'HST (15%): ${hst}', ln=True)
    pdf.cell(0, 10, f'Total: ${total:.2f}', ln=True)

    if notes:
        pdf.ln(10)
        pdf.multi_cell(0, 10, f'Notes: {notes}')

    pdf_file = f'{purchaser}-receipt.pdf'
    pdf.output(pdf_file, 'F')

    return pdf_file

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

        ReceiptModel.objects.create(
            company=company,
            purchaser=purchaser,
            product=product,
            price=price,
            quantity=quantity,
            hst=hst,
            notes=notes,
            total=total
        )

        pdf_file = create_pdf(company, purchaser, product, price, quantity, calculate_tax(), notes, total)

        with open(pdf_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{pdf_file}"'
            return response

    return render(request, 'dashboard/index.html')