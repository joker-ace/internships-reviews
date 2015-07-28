# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_companyinternshipreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='least_liked_things',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='most_liked_things',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='tasks',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
