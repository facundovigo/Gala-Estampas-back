from django.db import models

class Event(models.Model):
    title = models.TextField(default='Titulo evento')
    description = models.TextField('Descripcion', blank=True, null=True)
    event_picture = models.ImageField(verbose_name='Foto de evento', upload_to='evebt_pictures', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'