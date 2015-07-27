# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_auto_20150726_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='province',
        ),
    ]
