# Generated by Django 3.1 on 2020-09-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200918_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default='', verbose_name='Descripción'),
        ),
    ]
