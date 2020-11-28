from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('user', 'birthdate', 'address', 'city', 'state', 'country', 'zip_code', 'telephone')
    icon_name = 'person'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('client', 'product', 'cant', 'ticket', 'deposit', 'date_order', 'date_delivery', 'product_status')
    icon_name = 'shop'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'supply', 'photo', 'price')
    icon_name = 'card_giftcard'


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    fields = ('component', 'cant_per_prod')
    icon_name = 'assignment'


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    fields = ('code', 'description', 'replacement_price', 'stock')
    icon_name = 'local_shipping'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'icon')
    icon_name = 'category'

@admin.register(ZipAmount)
class ZipAmountAdmin(admin.ModelAdmin):
    fields = ('zip_code', 'amount')
    icon_name = 'monetization_on'
