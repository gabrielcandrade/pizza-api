from django_filters.rest_framework import DjangoFilterBackend
from flavorsApp.models import Flavor
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FlavorSerializer


class FlavorViewSet(ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filter_fields = ('name', 'value', 'description')
    search_fields = ('name', 'value', 'description')