# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20150726_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='city',
            new_name='cities',
        ),
    ]
