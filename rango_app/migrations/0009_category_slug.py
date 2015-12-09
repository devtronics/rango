# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango_app', '0008_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 12, 8, 23, 52, 2, 560257, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
