from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ('id', 'status', 'value')
    list_display_links = ('status',)
    readonly_fields = ('in_production_at', 'on_delivery_at', 'delivered_at')
    exclude = ('value', )