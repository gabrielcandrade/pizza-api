from pizzasApp.models import Pizza
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PizzaSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('flavor',)
