from rest_framework import serializers
from .models import *
from users.models import User
from users.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'user', 'birthdate', 'adress', 'city', 'state', 'country', 'zipcode', 'telephone')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'code', 'description', 'replacement_price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')


class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer(many=False, read_only=True, source='category')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category_id', 'category', 'article', 'photo', 'price')


class OrderSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=False, read_only=True, source='product')

    class Meta:
        model = Order
        fields = ('id', 'client', 'product_id', 'product', 'cant', 'date_order', 'date_delivery', 'deposit')


class FavoriteSerializer(serializers.ModelSerializer):
    #product_id = ProductSerializer(many=True, read_only=True, source='product')
    #client_id = UserSerializer(many=True, read_only=True, source='client')
    class Meta:
        model = Favorite
        fields = ('id', 'client', 'product')

