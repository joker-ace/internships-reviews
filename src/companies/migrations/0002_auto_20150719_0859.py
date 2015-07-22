# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.random_file_name


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_image',
            field=models.ImageField(null=True, upload_to=utils.random_file_name.RandomFileName(b'companies')),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
