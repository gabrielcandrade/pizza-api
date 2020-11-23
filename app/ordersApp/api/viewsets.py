import json

from ordersApp.models import Order
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED, HTTP_200_OK
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('client', 'status')

    # HTTP PUT
    def update(self, request, *args, **kwargs):
        order = Order.objects.get(pk = kwargs.get('pk'))
        data = {}
        if (order.status == 'on_delivery' or order.status == 'delivered'):
            data['message'] = "The order: " + str(order.id) + " just left for delivery or has already been delivered, cannot be updated! Sorry."
            return Response(data, status=HTTP_405_METHOD_NOT_ALLOWED)
        return super(OrderViewSet, self).update(request, *args, **kwargs)

    # HTTP PATCH
    def partial_update(self, request, *args, **kwargs):
        order = Order.objects.get(pk = kwargs.get('pk'))
        data = {}
        if (order.status == 'on_delivery' or order.status == 'delivered'):
            data['message'] = "The order: " + str(order.id) + " just left for delivery or has already been delivered, cannot be updated! Sorry."
            return Response(data, status=HTTP_405_METHOD_NOT_ALLOWED)
        return super(OrderViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['POST'], detail=True)
    def next_status(self, request, pk=None):
        order = Order.objects.get(pk = pk)
        data = {}
        data['message'] = "Order has been already delivered"
        now = timezone.now()

        if (order.status == 'in_queue'):
            order.status = 'in_production'
            order.in_production_at = now
            data['message'] = "Order: " + pk + " is now " + order.get_status_display() + " - Actual time: " + str(order.in_production_at)

        elif (order.status == 'in_production'):
            order.status = 'on_delivery'
            order.on_delivery_at = now
            data['message'] = "Order: " + pk + " is now " + order.get_status_display() + " - Actual time: " + str(order.on_delivery_at)

        elif (order.status == 'on_delivery'):
            order.status = 'delivered'
            order.delivered_at = now
            data['message'] = "Order: " + pk + " is now " + order.get_status_display() + " - Actual time: " + str(order.delivered_at)

        order.save()

        return Response(data, status=HTTP_200_OK)

    # This method would be open to user to track your order status
    @action(methods=['GET'], detail=True)
    def track(self, request, pk=None):
        order = Order.objects.get(pk = pk)
        data = {}
        data['message'] = "Your order has been delivered, nice meal, i hope you liked it :)"
        if (order.delivered_at):
            data['delivered_at'] = order.delivered_at
        else:
            data['message'] = "Your order still on delivery, anytime will arrive.."
        if (order.on_delivery_at):
            data['on_delivery_at'] = order.on_delivery_at
        else:
            data['message'] = "Your order still in production, anytime will update.."
        if (order.in_production_at):
            data['in_production_at'] = order.in_production_at
        else:
            data['message'] = "Your order still in queue, anytime will update.."

        return Response(data, status=HTTP_200_OK)