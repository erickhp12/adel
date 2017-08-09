# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-08 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='nombre(s)')),
                ('contacto', models.CharField(max_length=150, verbose_name='contacto(s)')),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name='telefono')),
                ('correo', models.EmailField(max_length=100, null=True, verbose_name='correo')),
                ('direccion', models.CharField(max_length=150, null=True, verbose_name='direccion')),
                ('producto', models.CharField(max_length=200, null=True, verbose_name='productos/servicios')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='fecha_inicio')),
            ],
        ),
    ]
