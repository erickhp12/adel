# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-28 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0006_auto_20170728_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='alergias_comentarios',
            field=models.CharField(max_length=200, null=True, verbose_name='describa'),
        ),
        migrations.AddField(
            model_name='historial',
            name='medicamentos_comentarios',
            field=models.CharField(max_length=200, null=True, verbose_name='describa'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Otros', 'Otros')], max_length=20, null=True, verbose_name='estado civil'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='ocupacion',
            field=models.CharField(max_length=50, null=True, verbose_name='ocupacion'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10, null=True, verbose_name='sexo'),
        ),
    ]