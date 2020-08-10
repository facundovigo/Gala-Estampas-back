from django.contrib import admin
from .models import Producto, Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    fields = ('cliente', 'fecha_pedido', 'fecha_entrega')
    icon_name = 'shop'


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fields = ('nombre', 'descripcion', 'estampa', 'inscripcion', 'cantidad', 'pedido', 'precio')
    icon_name = 'card_giftcard'
