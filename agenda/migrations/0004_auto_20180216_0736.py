# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-16 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_agenda_confirmacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='confirmacion',
            field=models.CharField(choices=[(b'Pendiente', b'Pendiente'), (b'Confirmada', b'Confirmada'), (b'Cancelada', b'Cancelada')], default=b'Pendiente', max_length=15, null=True, verbose_name='tipo de pago'),
        ),
    ]
