# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-14 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='contacto',
            field=models.CharField(max_length=150, null=True, verbose_name='contacto(s)'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=150, verbose_name='nombre(s)'),
        ),
    ]