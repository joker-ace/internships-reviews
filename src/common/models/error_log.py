# -*- coding: utf-8 -*-
from django.db import models

class ErrorLog(models.Model):
    error_url = models.CharField(max_length=255)
    stacktrace = models.TextField()
    date = models.DateTimeField(auto_now=True)