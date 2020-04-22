from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .managers import CustomUserManager


class NameModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    if settings.AUTH_WITH_EMAIL:
        REQUIRED_FIELDS = []
        objects = CustomUserManager()
        USERNAME_FIELD = 'email'
        email = models.EmailField(max_length=254, unique=True)
    else:
        pass


class Event(models.Model):
    title = models.TextField(default='Titulo evento')
    description = models.TextField('Descripcion', blank=True, null=True)
    event_picture = models.ImageField(verbose_name='Foto de evento', upload_to='evebt_pictures', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'