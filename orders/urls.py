from django.urls import path
from .views import (
    admin_dashboard,
    place_order,
    my_orders,
    order_report,
    invoice_report,
    sales_report
)

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('place-order/<int:tiffin_id>/', place_order, name='place_order'),
    path('my-orders/', my_orders, name='my_orders'),

    # REPORTS
    path('order-report/', order_report, name='order_report'),
    path('invoice-report/', invoice_report, name='invoice_report'),
    path('sales-report/', sales_report, name='sales_report'),
]
