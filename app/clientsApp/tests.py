import datetime

from addressApp.models import Address
from django.test import TestCase
from rest_framework.status import HTTP_201_CREATED

from .models import Client


# Create your tests here.
class ClientTest(TestCase):
    def test_create_client(self):
        address, created = Address.objects.get_or_create(
            line1 = "Rua Marechal Floriano Peixoto", 
            city = "Joao Pessoa",
            state_province = "Paraiba",
            postal_code = "58401311",
            country = "Brazil"
            )
        response = self.client.post('http://localhost:8005/api/client/', 
            {'address': address.id, 
             'name':"Gabriel Andrade", 
             'birth_date': "1995-05-22", 
             'is_vip': True
            }, format='json')
        client = Client.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(client.address.id, address.id)
        self.assertEqual(client.name, "Gabriel Andrade")
        self.assertEqual(client.birth_date, datetime.date(1995, 5, 22))
        self.assertEqual(client.is_vip, True)