# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-02 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(default=b'', max_length=300, null=True, verbose_name='motivo')),
                ('fecha_agenda', models.DateTimeField(verbose_name='fecha programada')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
            ],
        ),
    ]
