# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name']},
        ),
    ]