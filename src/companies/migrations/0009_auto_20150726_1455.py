# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_auto_20150726_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.ManyToManyField(to='common.City', db_table=b'company_office'),
        ),
    ]
