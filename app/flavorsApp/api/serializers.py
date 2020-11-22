from rest_framework.serializers import ModelSerializer
from flavorsApp.models import Flavor

class FlavorSerializer(ModelSerializer):
    class Meta:
        model = Flavor
        fields = ('id', 'name', 'description', 'value')