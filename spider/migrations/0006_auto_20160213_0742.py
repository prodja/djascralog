# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0005_auto_20160212_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_gb',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
