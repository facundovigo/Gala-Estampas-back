from django.db import models
from users.models import User
import datetime
from django.utils import timezone

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, default=None) #este usr vamos a tener q modificarlo porq es el base
    fecha_pedido = models.DateField(default=datetime.date.today)
    fecha_entrega = models.DateField(default=datetime.date.today() + timezone.timedelta(days=5))
    adelanto = models.IntegerField(default=0)
    factura = models.IntegerField(default=0) #esto tmb puede ser un modelo

    def __str__(self):
        return f'{self.cliente} {self.fecha_entrega}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Producto(models.Model):
    nombre = models.TextField(default='')
    descripcion = models.TextField('descripcion', blank=True, null=True)
    insumo = models.TextField('descripcion', blank=True, null=True) #va a ser un modelo
    estampa = models.ImageField(verbose_name='Estampa de producto', upload_to='producto_estampa', blank=True, null=True)
    inscripcion = models.TextField('inscripcion', blank=True, null=True)
    foto = models.ImageField(verbose_name='Foto de producto', upload_to='producto_foto', blank=True, null=True)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=1)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

