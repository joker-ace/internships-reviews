# -*- coding: utf-8 -*-
from django.db import models

from utils.random_file_name import RandomFileName
from common.models.city import City


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    cities = models.ManyToManyField(City, db_table='company_office')
    logo_image = models.ImageField(
        upload_to=RandomFileName('companies'), null=True,
        default='/static/logo_default.png')

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'Companies'

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name
        }
