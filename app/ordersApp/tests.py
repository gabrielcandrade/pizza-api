from django.test import TestCase
from .models import Order
from flavorsApp.models import Flavor
from sizesApp.models import Size
from pizzasApp.models import Pizza
from clientsApp.models import Client
from addressApp.models import Address
from rest_framework.status import HTTP_201_CREATED
from decimal import Decimal

# Create your tests here.
class OrderTest(TestCase):
    def test_create_order(self):
        address, created = Address.objects.get_or_create(
            line1 = "Rua Vigolvino Wanderley, 194, Conceição",
            city = "Campina Grande",
            state_province = "Paraíba",
            postal_code = "58401311",
            country = "Brazil"
        )
        client, created = Client.objects.get_or_create(
            address = address,
            name = "Gabriel Andrade",
            birth_date = "1995-05-22",
            is_vip = True
        )
        flavor1, created = Flavor.objects.get_or_create(
            name = "Pepperoni",
            value = 35.78,
            description = "A traditional flavor based on italian style"
        )
        flavor2, created = Flavor.objects.get_or_create(
            name = "Margarita",
            value = 32.64,
            description = "All vegetables here are fresh and juicy"
        )
        size1, created = Size.objects.get_or_create(
            name = "Large",
            value = 25.54,
            slices = 8,
            description = "For a hole family"
        )
        size2, created = Size.objects.get_or_create(
            name = "Small",
            value = 5.88,
            slices = 4,
            description = "For one person"
        )
        pizza1, created = Pizza.objects.get_or_create(
            flavor = flavor1,
            size = size1,
            quantity = 5
        )
        pizza2, created = Pizza.objects.get_or_create(
            flavor = flavor2,
            size = size2,
            quantity = 3
        )
        response = self.client.post('http://localhost:8005/api/order/', 
            {'client': client.id, 
             'pizzas': [pizza1.id, pizza2.id]
            }, format='json')
        order = Order.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(order.client.id, client.id)
        self.assertEqual(order.pizzas.get(pk=pizza1.id), pizza1)
        self.assertEqual(order.pizzas.get(pk=pizza2.id), pizza2)