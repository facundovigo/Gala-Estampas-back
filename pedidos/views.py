from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Pedido
from .serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()