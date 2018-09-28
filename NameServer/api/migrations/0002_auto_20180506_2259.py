# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-06 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='location',
            name='port',
        ),
        migrations.AddField(
            model_name='location',
            name='URI',
            field=models.CharField(default=102, max_length=100),
            preserve_default=False,
        ),
    ]