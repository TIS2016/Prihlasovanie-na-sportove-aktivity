# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooluser',
            name='login',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='function',
            field=models.BooleanField(default=False),
        ),
    ]