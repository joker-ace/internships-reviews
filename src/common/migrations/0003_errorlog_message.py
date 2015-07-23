# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_errorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorlog',
            name='message',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
