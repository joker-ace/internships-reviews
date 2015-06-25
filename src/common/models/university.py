# -*- coding: utf-8 -*-
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name