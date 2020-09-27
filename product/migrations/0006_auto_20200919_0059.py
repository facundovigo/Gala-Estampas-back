# Generated by Django 3.1 on 2020-09-19 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200918_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(max_length=20, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.DateField(default=datetime.date(2020, 9, 24), verbose_name='Fecha de Entrega'),
        ),
    ]