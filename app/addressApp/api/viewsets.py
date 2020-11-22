from django_filters.rest_framework import DjangoFilterBackend
from addressApp.models import Address
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # Filter plugin
    filter_backends = (DjangoFilterBackend,SearchFilter,)
    filter_fields = ('city', 'state_province', 'postal_code', 'country')
    search_fields = ('line1', 'line2', 'city', 'state_province', 'country')