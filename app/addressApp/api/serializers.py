from rest_framework.serializers import ModelSerializer
from addressApp.models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'line2', 'city', 'state_province', 'postal_code', 'country')