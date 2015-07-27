# -*- coding: utf-8 -*-

from django.db import models
from common.models.province import Province


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    province = models.ForeignKey(Province, null=True)

    class Meta:
        db_table = 'city'
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.name + (self.province and ', ' + self.province.name)
