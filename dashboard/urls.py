from django.urls import path
from .views import index, create_receipt_view

app_name = "dashboard"

urlpatterns = [
    path('', index, name='index'),
    path('create-pdf/', create_receipt_view, name="create-pdf")
]