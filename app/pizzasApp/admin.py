from django.contrib import admin
from .models import Pizza

# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin): 
    list_display = ('id', 'flavor', 'size', 'quantity', 'value')
    list_display_links = ('flavor',)
    exclude = ('value',)