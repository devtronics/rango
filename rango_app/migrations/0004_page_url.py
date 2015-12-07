# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango_app', '0003_auto_20151207_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(default=datetime.datetime(2015, 12, 7, 1, 1, 45, 781942, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
