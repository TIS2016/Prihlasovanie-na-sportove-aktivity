# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170108_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='function',
            field=models.BooleanField(),
        ),
    ]
