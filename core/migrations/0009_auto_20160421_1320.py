# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160421_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='thread',
            name='content',
            field=models.TextField(),
        ),
    ]