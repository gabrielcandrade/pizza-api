from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ('id', 'status', 'value')
    list_display_links = ('status',)
    exclude = ('value',)