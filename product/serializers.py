from rest_framework import serializers
from .models import *
from users.models import User
from users.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'user', 'birthdate', 'address', 'city', 'state', 'country', 'zip_code', 'telephone')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'code', 'description', 'replacement_price', 'stock')


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ('id', 'component', 'cant_per_prod')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')


class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer(many=False, read_only=True, source='category')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category_id', 'category', 'supply', 'photo', 'price')


class OrderSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=False, read_only=True, source='product')

    class Meta:
        model = Order
        fields = ('id',
                  'client',
                  'product_id',
                  'product',
                  'cant',
                  'date_order',
                  'date_delivery',
                  'deposit',
                  'product_status')


class FavoriteSerializer(serializers.ModelSerializer):
    client_id = UserSerializer(many=False, read_only=True, source='client')
    product_id = ProductSerializer(many=False, read_only=True, source='product')

    class Meta:
        model = Favorite
        fields = ('id', 'client', 'product', 'client_id', 'product_id')


class ZipAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipAmount
        fields = ('id', 'zip_code', 'amount')
