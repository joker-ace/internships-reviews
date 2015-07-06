# -*- coding: utf-8 -*-
from django.db import models

from common.models.university import University


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name + ', ' + self.university.name

    def __str__(self):
        return unicode(self)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ["university", "name"]
