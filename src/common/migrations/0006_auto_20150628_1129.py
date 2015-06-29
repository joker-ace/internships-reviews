# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150628_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='university',
        ),
        migrations.AddField(
            model_name='university',
            name='province',
            field=models.ForeignKey(default=None, to='common.Province'),
        ),
    ]
