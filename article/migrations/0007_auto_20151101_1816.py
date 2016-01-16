# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from random import randrange

def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Comment = apps.get_model("article", "Comments")
    usr=apps.get_model("auth", "User")

    for comment in Comment.objects.all():
    	id=randrange(1,2)
        comment.comments_from = usr.objects.all()[id]
        comment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comments_comments_from'),
    ]

    operations = [
migrations.RunPython(combine_names),
    ]
