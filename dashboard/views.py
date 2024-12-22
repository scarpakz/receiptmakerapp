from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')

def create_pdf(request):
    return None

def create_receipt_view(request):
    return None