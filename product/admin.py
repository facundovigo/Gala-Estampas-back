from django.contrib import admin
from .models import Product, Order, Article


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('client', 'product', 'cant', 'deposit', 'date_order', 'date_delivery')
    icon_name = 'shop'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'article', 'stamp', 'inscription', 'price')
    icon_name = 'card_giftcard'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'replacement_price')
    icon_name = 'card_giftcard'
