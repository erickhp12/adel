# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-27 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='estado',
        ),
    ]