# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ['university', 'name'], 'verbose_name': 'Faculty', 'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='university',
            old_name='seat_of_rectorate',
            new_name='city',
        ),
    ]
