# Generated by Django 3.1 on 2020-09-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200927_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]
