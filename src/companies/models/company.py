# -*- coding: utf-8 -*-
from django.db import models

from utils.random_file_name import RandomFileName
from common.models.province import Province


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(Province, null=True)
    city = models.CharField(max_length=255, null=True)
    logo_image = models.ImageField(
        upload_to=RandomFileName('companies'), null=True,
        default='/static/logo_default.png'
    )

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'Companies'

    def __unicode__(self):
        return self.name
