from django.contrib import admin
from .models import Order
from invoices.models import Invoice

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'order_date')
    list_filter = ('status',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Generate invoice when order is delivered
        if obj.status == 'DELIVERED':
            Invoice.objects.get_or_create(
                order=obj,
                defaults={
                    'invoice_number': f"INV-{obj.id}"
                }
            )
