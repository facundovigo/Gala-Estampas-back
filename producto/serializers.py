from rest_framework import serializers
from .models import Producto


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'title', 'description', 'event_picture')