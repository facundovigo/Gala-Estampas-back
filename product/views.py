from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Order, Product, Article
from .serializers import OrderSerializer, ProductSerializer, ArticleSerializer
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=False)
    def search_product(self, request):
        queryset = Product.objects.all().order_by('name')
        search_name = self.request.query_params.get('search_name')
        print(search_name)
        if search_name:
            queryset = queryset.filter(name__icontains=search_name).order_by('name')

        #page = self.paginate_queryset(queryset)
        #if page is not None:
            #serializer = self.get_serializer(page, many=True)
            #return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
