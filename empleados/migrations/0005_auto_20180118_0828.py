# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-18 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_empleado_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='edad',
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateTimeField(null=True, verbose_name=b'fecha_nacimiento'),
        ),
    ]