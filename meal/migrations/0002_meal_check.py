# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-27 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]