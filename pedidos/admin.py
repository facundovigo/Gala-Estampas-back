from django.contrib import admin
from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'event_picture')
    icon_name = 'shop'
    name = 'Compras'