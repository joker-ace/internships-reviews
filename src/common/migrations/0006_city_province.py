# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(to='common.Province', null=True),
        ),
    ]
