# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Company Name')
    logo_image = models.ImageField(upload_to='media_content/', default='images/logo_default.png')
