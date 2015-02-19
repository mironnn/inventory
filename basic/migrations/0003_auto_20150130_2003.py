# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20150130_1953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='serial_number',
            new_name='device_type',
        ),
        migrations.RenameField(
            model_name='device_type',
            old_name='serial_number',
            new_name='type',
        ),
    ]
