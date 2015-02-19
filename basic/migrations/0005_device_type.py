# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_auto_20150130_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.ForeignKey(default=1, to='basic.device_type'),
            preserve_default=False,
        ),
    ]
