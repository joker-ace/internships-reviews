# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='university',
            field=models.ForeignKey(default=0, to='common.University'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='seat_of_rectorate',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
