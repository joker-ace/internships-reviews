# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_errorlog_message'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='errorlog',
            table='error_log',
        ),
    ]
