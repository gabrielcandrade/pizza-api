from django.test import TestCase
from .models import Flavor
from rest_framework.status import HTTP_201_CREATED
from decimal import Decimal

# Create your tests here.
class FlavorTest(TestCase):
    def test_create_flavor(self):
        response = self.client.post('http://localhost:8005/api/flavor/', 
            {'name': 'Pepperoni', 
             'value': 35.78, 
             'description': "A traditional flavor based on italian style"
            }, format='json')
        flavor = Flavor.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(flavor.name, "Pepperoni")
        self.assertEqual(flavor.value, Decimal('35.78'))
        self.assertEqual(type(flavor.value), Decimal)
        self.assertEqual(flavor.description, "A traditional flavor based on italian style")