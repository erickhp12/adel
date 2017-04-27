# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-26 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(max_length=200, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=100, null=True, unique=True, verbose_name='correo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha_inicio'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(max_length=200, unique=True, verbose_name='nombres'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='puesto',
            field=models.CharField(max_length=100, verbose_name='puesto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=100, null=True, verbose_name='telefono'),
        ),
    ]
