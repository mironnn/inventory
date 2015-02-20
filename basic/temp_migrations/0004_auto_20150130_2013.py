# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20150130_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='name',
            new_name='User',
        ),
    ]
