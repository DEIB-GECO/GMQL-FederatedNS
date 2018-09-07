# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-31 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_institution_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]