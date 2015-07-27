# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_city_province'),
        ('companies', '0007_auto_20150725_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='city',
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ManyToManyField(to='common.City'),
        ),
    ]
