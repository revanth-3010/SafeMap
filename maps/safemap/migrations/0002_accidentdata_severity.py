# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safemap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidentdata',
            name='severity',
            field=models.IntegerField(default=1),
        ),
    ]
