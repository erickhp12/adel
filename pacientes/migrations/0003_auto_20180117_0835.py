# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='edad',
        ),
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de nacimiento'),
        ),
    ]
