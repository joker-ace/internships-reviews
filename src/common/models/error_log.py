# -*- coding: utf-8 -*-
from django.db import models

class ErrorLog(models.Model):
    error_url = models.CharField(max_length=255)
    message = models.CharField(max_length=255, default='')
    stacktrace = models.TextField()
    date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return 'Error log #{} from {}'.format(self.pk, self.date.strftime('%d-%m-%Y %H:%M'))