# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 16:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0003_auto_20160212_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_gb',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 12, 16, 46, 42, 780674)),
        ),
    ]
