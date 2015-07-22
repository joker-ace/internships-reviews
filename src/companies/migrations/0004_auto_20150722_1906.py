# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.random_file_name


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150722_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo_image',
            field=models.ImageField(default=b'/static/logo_default.png', null=True, upload_to=utils.random_file_name.RandomFileName(b'companies')),
        ),
    ]
