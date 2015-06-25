# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150625_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='province',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
    ]
