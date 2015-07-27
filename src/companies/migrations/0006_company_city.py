# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_city'),
        ('companies', '0005_remove_company_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(to='common.City', null=True),
        ),
    ]
