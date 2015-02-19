# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20150130_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='date',
        ),
        migrations.AddField(
            model_name='device',
            name='date_finish',
            field=models.DateTimeField(default=timezone.now(), verbose_name=b'Finish warranty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='date_start',
            field=models.DateTimeField(default=timezone.now(), verbose_name=b'Start warranty'),
            preserve_default=False,
        ),
    ]
