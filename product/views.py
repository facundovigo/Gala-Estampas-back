from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.http import JsonResponse


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user')

        if user_id:
            self.queryset = self.queryset.filter(user=user_id)

        return self.queryset


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination

    @action(detail=False)
    def search_product(self, request):
        queryset = Product.objects.all().order_by('name')
        search_name = self.request.query_params.get('search_name')
        search_category = self.request.query_params.get('search_category')
        if search_name:
            queryset = queryset.filter(name__icontains=search_name).order_by('name')
        if search_category:
            queryset = queryset.filter(category__id=search_category).order_by('name')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class OrderPagination(PageNumberPagination):
    page_size = 5


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = OrderPagination

    @action(detail=False)
    def search_order(self, request):
        queryset = Order.objects.all().order_by('date_delivery')
        client_id = self.request.query_params.get('client_id')
        if client_id:
            queryset = queryset.filter(client__id__icontains=client_id).order_by('-date_delivery')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class FavoritePagination(PageNumberPagination):
    page_size = 5


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    pagination_class = FavoritePagination

    @action(detail=False)
    def search_by_user_id(self, request):
        client_id = self.request.query_params.get('client_id')

        if client_id:
            queryset = Favorite.objects.filter(client=client_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def verify(self, request):
        client_id = self.request.query_params.get('client_id')
        product_id = self.request.query_params.get('product_id')
        if client_id and product_id:
            queryset = Favorite.objects.filter(client=client_id, product=product_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def delete(self, request):
        user_id = self.request.query_params.get('user_id')
        product_id = self.request.query_params.get('product_id')
        if user_id and product_id:
            Favorite.objects.filter(client=user_id, product=product_id).delete()
            return HttpResponse(status=200)
        return JsonResponse({'error': 'something bad'}, status=400)
