# -*- coding: utf-8 -*-
from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'province'
        ordering = ['name']

    def __unicode__(self):
        return self.name
