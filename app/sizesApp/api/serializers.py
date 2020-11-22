from rest_framework.serializers import ModelSerializer
from sizesApp.models import Size

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name', 'value', 'slices', 'description')