from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime

from accounts.models import Customer
from tiffin.models import Tiffin
from .models import Order
from invoices.models import Invoice


# ===================== ADMIN DASHBOARD =====================
def admin_dashboard(request):
    total_users = Customer.objects.count()
    total_tiffins = Tiffin.objects.count()
    total_orders = Order.objects.count()

    confirmed_orders = Order.objects.filter(status='CONFIRMED').count()
    cancelled_orders = Order.objects.filter(status='CANCELLED').count()
    delivered_orders = Order.objects.filter(status='DELIVERED').count()

    total_invoices = Invoice.objects.count()

    total_sales = Order.objects.filter(
        status='DELIVERED'
    ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'total_users': total_users,
        'total_tiffins': total_tiffins,
        'total_orders': total_orders,
        'confirmed_orders': confirmed_orders,
        'cancelled_orders': cancelled_orders,
        'delivered_orders': delivered_orders,
        'total_invoices': total_invoices,
        'total_sales': total_sales,
    }

    return render(request, 'admin/dashboard.html', context)


# ===================== PLACE ORDER =====================
def place_order(request, tiffin_id):
    if 'user_id' not in request.session:
        return redirect('/accounts/login/')

    customer = Customer.objects.get(id=request.session['user_id'])
    tiffin = Tiffin.objects.get(id=tiffin_id)

    Order.objects.create(
        customer=customer,
        total_amount=tiffin.price,
        status='NEW'
    )

    return redirect('/my-orders/')


# ===================== MY ORDERS =====================
def my_orders(request):
    if 'user_id' not in request.session:
        return redirect('/accounts/login/')

    customer = Customer.objects.get(id=request.session['user_id'])
    orders = Order.objects.filter(customer=customer).order_by('-order_date')

    return render(request, 'user/my_orders.html', {'orders': orders})


# ===================== ORDER REPORT =====================
def order_report(request):
    orders = []
    if request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        orders = Order.objects.filter(
            order_date__date__range=[from_date, to_date]
        )

    return render(request, 'admin/order_report.html', {'orders': orders})


# ===================== INVOICE REPORT =====================
def invoice_report(request):
    invoices = []
    if request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        invoices = Invoice.objects.filter(
            created_at__date__range=[from_date, to_date]
        )

    return render(request, 'admin/invoice_report.html', {'invoices': invoices})


# ===================== SALES REPORT =====================
def sales_report(request):
    total_sales = 0
    if request.method == 'POST':
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        total_sales = Order.objects.filter(
            status='DELIVERED',
            order_date__date__range=[from_date, to_date]
        ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    return render(request, 'admin/sales_report.html', {'total_sales': total_sales})
