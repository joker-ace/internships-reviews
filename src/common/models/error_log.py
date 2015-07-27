# -*- coding: utf-8 -*-
from django.db import models

class ErrorLog(models.Model):
    error_url = models.CharField(max_length=255)
    message = models.CharField(max_length=255, default='')
    stacktrace = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'error_log'

    def __unicode__(self):
        return '{} | {}'.format(self.date.strftime('%d-%m-%Y %H:%M'), self.error_url)