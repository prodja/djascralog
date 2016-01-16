# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20151101_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelTable(
            name='article',
            table='\u0421\u0442\u0430\u0442\u044c\u0438',
        ),
    ]
