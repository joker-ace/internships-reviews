# -*- coding: utf-8 -*-
from django.db import models
from common.models.university import University


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name