from django.contrib import admin
from .models import Tiffin

@admin.register(Tiffin)
class TiffinAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)
