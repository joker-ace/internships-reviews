# -*- coding: utf-8 -*-
from django.db import models
from common.models.province import Province

class University(models.Model):
    name = models.CharField(max_length=255)
    seat_of_rectorate = models.CharField(max_length=50)
    province = models.ForeignKey(Province, default=None)

    def __unicode__(self):
        return self.name