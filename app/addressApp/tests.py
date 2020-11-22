from django.test import TestCase
from .models import Address
from rest_framework.status import HTTP_201_CREATED

# Create your tests here.
class AddressTest(TestCase):
    def test_create_address(self):
        response = self.client.post('http://localhost:8005/api/address/', 
            {'line1': 'Rua Marechal Floriano Peixoto', 
             'city': "Joao Pessoa", 
             'state_province': "Paraiba", 
             'postal_code': '58401311', 
             'country': "Brazil"
            }, format='json')
        address = Address.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(address.line1, "Rua Marechal Floriano Peixoto")
        self.assertEqual(address.city, "Joao Pessoa")
        self.assertEqual(address.state_province, "Paraiba")
        self.assertEqual(address.postal_code, "58401311")
        self.assertEqual(address.country, "Brazil")