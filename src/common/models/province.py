# -*- coding: utf-8 -*-
from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return unicode(self)
