# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0010_auto_20150219_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='User',
            field=models.ForeignKey(to='basic.user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='date_finish',
            field=models.DateTimeField(verbose_name=b'Finish warranty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='date_start',
            field=models.DateTimeField(verbose_name=b'Start warranty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='device_name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(to='basic.device_type'),
            preserve_default=True,
        ),
    ]
