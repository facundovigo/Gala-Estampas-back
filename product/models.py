from django.db import models
from users.models import User
import datetime
from django.utils import timezone


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


class Article(models.Model):
    code = models.CharField(unique=True, max_length=20, verbose_name='Código')
    description = models.TextField(default='', verbose_name='Descripción')
    replacement_price = models.IntegerField(default=0, verbose_name='Precio de reposición')

    def __str__(self):
        return f'({self.code}) + {self.description}'

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'


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
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Artículo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    photo = models.ImageField(upload_to='product_photo', blank=True, null=True, verbose_name='Foto de producto')
    price = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Cliente') #este usr vamos a tener q modificarlo porq es el base
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    cant = models.IntegerField(default=1, verbose_name='Cantidad')
    date_order = models.DateField(default=datetime.date.today, verbose_name='Fecha de Pedido')
    date_delivery = models.DateField(default=datetime.date.today() + timezone.timedelta(days=5), verbose_name='Fecha de Entrega')
    deposit = models.IntegerField(default=0, verbose_name='Adelanto')
    ticket = models.IntegerField(default=0, verbose_name='Factura') #esto tmb puede ser un modelo

    def __str__(self):
        return f'{self.client} {self.date_delivery}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Favorite(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return f'{self.client} - {self.product}'

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
