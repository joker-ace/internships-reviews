# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('common', '0002_auto_20150630_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_studying', models.BooleanField(default=False)),
                ('faculty', models.ForeignKey(to='common.Faculty')),
                ('university', models.ForeignKey(to='common.University')),
            ],
        ),
    ]
