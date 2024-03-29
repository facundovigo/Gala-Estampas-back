from django.db import models
from django.shortcuts import get_object_or_404

from galaEstampas.settings import EMAIL_HOST_USER, BASE_DIR
from users.models import User
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    birthdate = models.DateField(verbose_name='fch Nacimiento')
    address = models.CharField(max_length=50, blank=True, null=True, verbose_name='Dirección')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ciudad')
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name='Provincia')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='País')
    zip_code = models.CharField(max_length=8, blank=True, null=True, verbose_name='Cód Postal')
    telephone = models.IntegerField(verbose_name='Teléfono')
    #instagram

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Component(models.Model):
    code = models.CharField(unique=True, max_length=20, verbose_name='Código')
    description = models.TextField(default='', verbose_name='Descripción')
    replacement_price = models.IntegerField(default=0, verbose_name='Precio de reposición')
    stock = models.IntegerField(default=0, verbose_name="Disponibles")

    def reduce_stock(self, cant):
        print('1', self.stock)
        self.stock = self.stock - cant
        print('2', self.stock)
        super(Component, self).save()

    def __str__(self):
        return f'({self.code}) - {self.description}'

    class Meta:
        verbose_name = 'Stock disponible'
        verbose_name_plural = 'Stock disponible'


class Supply(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True, verbose_name='Componente')
    cant_per_prod = models.IntegerField(default=1, verbose_name="Cantidad por por producto")

    def __str__(self):
        return f'{self.component.__str__()} - cant: {self.cant_per_prod}'

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def reduce_stock(self, cant):
        self.component.reduce_stock(cant * self.cant_per_prod)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Categoría')
    icon = models.ImageField(upload_to='icon_category', verbose_name='Ícono')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Product(models.Model):

    name = models.TextField(default='', verbose_name='Nombre')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, null=True, verbose_name='Insumo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    photo = models.ImageField(upload_to='product_photo', blank=True, null=True, verbose_name='Foto de producto')
    price = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def reduce_stock(self, cant):
        self.supply.reduce_stock(cant)


class Order(models.Model):

    class ProductStatus(models.TextChoices):
        ORDER = 'OR', _('Pedido')
        ACCEPT = 'AC', _('Aceptado')
        IN_PROCESS = 'PR', _('En proceso')
        FINISHED = 'FN', _('Terminado')
        DELIVERED = 'DE', _('Entregado')
        REJECT = 'RJ', _('Rechazado')
        CANCELED = 'CC', _('Cancelado')

    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Cliente')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    cant = models.IntegerField(default=1, verbose_name='Cantidad')
    date_order = models.DateField(default=datetime.date.today, verbose_name='Fecha de Pedido')
    date_delivery = models.DateField(default=datetime.date.today() + timezone.timedelta(days=5), verbose_name='Fecha de Entrega')
    deposit = models.IntegerField(default=0, verbose_name='Adelanto')
    ticket = models.IntegerField(default=0, verbose_name='Monto Total')
    product_status = models.CharField(
        max_length=2,
        choices=ProductStatus.choices,
        default=ProductStatus.ORDER,
    )

    def __str__(self):
        return f'Pedido Nro: {self.id}, Cliente: {self.client.first_name}, Fecha de entrega: {self.date_delivery}'

    def save(self, *args, **kwargs):
        usr = self.client.email
        self.price()
        if getattr(self, 'product_status') == Order.ProductStatus.ORDER:
            html_message = render_to_string('mail_template_order_create.html',
                                            {'order_num': self.id, 'product': self.product})
            send_mail(
                f'Se ha creado tu pedido en galaestampas.ar',
                f'Gracias por elegirnos',
                'sirdemian@gmail.com',
                [usr],
                html_message=html_message,
                fail_silently=False
            )
        if getattr(self, 'product_status') == Order.ProductStatus.FINISHED:
            self.product.reduce_stock(self.cant)
            html_message = render_to_string('mail_template_finish_order.html', {'order_num': self.id})

            send_mail(
                f'Tu pedido {self.id} está en camino!!! GALA ESTAMPAS',
                f'Gracias por elegirnos',
                'sirdemian@gmail.com',
                [usr],
                html_message=html_message,
                fail_silently=False
            )
        super(Order, self).save(*args, **kwargs)

    def price(self):
        self.ticket = self.product.price * self.cant

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Favorite(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_r', verbose_name='Cliente')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_r', verbose_name='Producto')

    def __str__(self):
        return f'{self.client} - {self.product}'

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

class ZipAmount(models.Model):
    zip_code = models.CharField(unique=True, max_length=8, verbose_name='Cód Postal')
    amount = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return f'{self.zip_code} - ${self.amount}.-'

    class Meta:
        verbose_name = 'Costo de envío'
        verbose_name_plural = 'Costos de envíos'
