# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_printer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printer',
            name='device_ptr',
        ),
        migrations.DeleteModel(
            name='printer',
        ),
    ]
