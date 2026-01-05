from django.shortcuts import render, get_object_or_404
from .models import Invoice

def view_invoice(request, order_id):
    invoice = get_object_or_404(Invoice, order__id=order_id)
    return render(request, 'user/invoice.html', {'invoice': invoice})
