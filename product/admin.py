from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('user', 'birthdate', 'address', 'city', 'state', 'country', 'zip_code', 'telephone')
    icon_name = 'person'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('client', 'product', 'cant', 'deposit', 'date_order', 'date_delivery')
    icon_name = 'shop'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'article', 'photo', 'price')
    icon_name = 'card_giftcard'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('code', 'description', 'replacement_price')
    icon_name = 'card_giftcard'


@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'icon')
    icon_name = 'shop'

@admin.register(ZipAmount)
class ZipAmountAdmin(admin.ModelAdmin):
    fields = ('zip_code', 'amount')
    icon_name = 'geo'
