# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0006_city_province'),
        ('companies', '0011_remove_company_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInternshipReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommendation', models.IntegerField()),
                ('apply_skills', models.IntegerField()),
                ('learn_new', models.IntegerField()),
                ('tasks', models.TextField(default=None, null=True)),
                ('most_liked_things', models.TextField(default=None, null=True)),
                ('least_liked_things', models.TextField(default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(to='companies.Company')),
                ('office', models.ForeignKey(to='common.City')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'company_internship_review',
                'verbose_name': 'Company internship review',
                'verbose_name_plural': 'Company internships reviews',
            },
        ),
    ]
