from rest_framework.serializers import ModelSerializer
from pizzasApp.models import Pizza

class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'flavor', 'size', 'quantity', 'value')