# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango_app', '0004_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 12, 8, 22, 9, 50, 718501, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
