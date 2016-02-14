# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price_gb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('code', models.TextField(verbose_name='\u041a\u043e\u0434 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'db_table': 'price_gb',
                'verbose_name': '\u0426\u0435\u043d\u044b gb',
            },
        ),
    ]