from ordersApp.models import Order
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('client', 'pizzas', 'status')