from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Producto.objects.all()