from django.contrib import admin
from .models import ReceiptModel

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['company', 'price']

admin.site.register(ReceiptModel, ReceiptAdmin)