# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Precio'),
        ),
    ]