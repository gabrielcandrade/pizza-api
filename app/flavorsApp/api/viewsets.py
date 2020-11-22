from flavorsApp.models import Flavor
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FlavorSerializer


class FlavorViewSet(ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
