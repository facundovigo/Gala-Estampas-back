# Generated by Django 3.1 on 2020-11-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20201128_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]
