# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0004_auto_20160212_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_gb',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
