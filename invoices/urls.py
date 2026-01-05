from django.urls import path
from .views import view_invoice

urlpatterns = [
    path('invoice/<int:order_id>/', view_invoice, name='view_invoice'),
]
