from django.test import TestCase
from .models import Pizza
from flavorsApp.models import Flavor
from sizesApp.models import Size
from rest_framework.status import HTTP_201_CREATED
from decimal import Decimal

# Create your tests here.
class PizzaTest(TestCase):
    def test_create_pizza(self):
        flavor, created = Flavor.objects.get_or_create(
            name = "Pepperoni",
            value = 35.78,
            description = "A traditional flavor based on italian style"
        )
        size, created = Size.objects.get_or_create(
            name = "Large",
            value = 25.54,
            slices = 8,
            description = "For a hole family"
        )
        response = self.client.post('http://localhost:8005/api/pizza/', 
            {'flavor': flavor.id, 
             'size': size.id, 
             'quantity': 3
            }, format='json')
        pizza = Pizza.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(pizza.flavor.id, flavor.id)
        self.assertEqual(pizza.size.id, size.id)
        self.assertEqual(pizza.quantity, 3)
        self.assertEqual(type(pizza.value), Decimal)
        self.assertEqual(pizza.value, Decimal('183.96'))