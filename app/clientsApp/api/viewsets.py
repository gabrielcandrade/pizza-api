from django_filters.rest_framework import DjangoFilterBackend
from clientsApp.models import Client
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filter_fields = ('address', 'name', 'birth_date', 'client_since', 'is_vip')
    search_fields = ('name')