# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_auto_20150130_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='printer',
            fields=[
                ('device_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='basic.device')),
                ('comment', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=('basic.device',),
        ),
    ]
