# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151004_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(default=1, to='article.Article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(default=datetime.datetime(2015, 10, 4, 16, 59, 37, 515517, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
