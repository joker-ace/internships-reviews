# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.random_file_name


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_auto_20150728_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo_image',
            field=models.ImageField(default=b'/static/images/logo_default.png', null=True, upload_to=utils.random_file_name.RandomFileName(b'companies')),
        ),
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='apply_skills',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='learn_new',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='companyinternshipreview',
            name='recommendation',
            field=models.FloatField(),
        ),
    ]
