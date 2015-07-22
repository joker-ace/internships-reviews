# -*- coding: utf-8 -*-
from django.db import models

from common.models.university import University


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    university = models.ForeignKey(University)

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ["university", "name"]

    @classmethod
    def create(cls, name, university):
        return cls(name=name, university=university)

    def __unicode__(self):
        return self.name + ', ' + self.university.name
