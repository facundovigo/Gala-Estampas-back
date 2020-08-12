from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Order, Product, Article
from .serializers import OrderSerializer, ProductSerializer, ArticleSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()