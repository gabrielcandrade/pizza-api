from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED
from django.test import TestCase
from .models import Size

# Create your tests here.
class SizeTest(TestCase):
    def test_create_size(self):
        response = self.client.post('http://localhost:8005/api/size/', {
            'name': 'Small', 
            'value': 5.50, 
            'slices': 4, 
            'description': 'For kids'
        }, format='json')
        size = Size.objects.last()
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(size.name, "Small")
        self.assertEqual(size.value, 5.50)
        self.assertEqual(size.slices, 4)