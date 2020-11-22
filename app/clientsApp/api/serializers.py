from rest_framework.serializers import ModelSerializer
from clientsApp.models import Client

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('address', 'name', 'birth_date', 'client_since', 'is_vip')