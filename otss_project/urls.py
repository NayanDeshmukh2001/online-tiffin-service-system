from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    # USER SIDE
    path('', include('tiffin.urls')),

    # ORDERS + DASHBOARD + REPORTS
    path('', include('orders.urls')),

    # INVOICES
    path('', include('invoices.urls')),
]
