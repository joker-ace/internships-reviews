# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Company Name', unique=True, max_length=255)),
                ('logo_image', models.ImageField(default=b'images/logo_default.png', upload_to=b'media_content/')),
            ],
            options={
                'db_table': 'company',
                'managed': True,
            },
        ),
    ]
