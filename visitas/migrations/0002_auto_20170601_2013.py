# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-01 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitas',
            name='dolares',
            field=models.CharField(choices=[(b'Pesos', b'Pesos'), (b'Dolares', b'Dolares')], max_length=50, verbose_name='Divisa'),
        ),
    ]
