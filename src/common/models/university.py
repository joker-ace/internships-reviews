# -*- coding: utf-8 -*-
from django.db import models
from common.models.province import Province

class University(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    province = models.ForeignKey(Province, default=None)

    class Meta:
        db_table = 'university'
        ordering = ['name']
        verbose_name_plural = 'Universities'

    def __unicode__(self):
        return self.name
