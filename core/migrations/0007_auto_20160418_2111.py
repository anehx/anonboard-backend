# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160416_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
    ]
