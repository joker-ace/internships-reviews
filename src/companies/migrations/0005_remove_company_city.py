# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20150722_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
    ]
