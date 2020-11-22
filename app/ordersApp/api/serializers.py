from rest_framework.serializers import ModelSerializer
from ordersApp.models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'pizzas', 'status', 'value')