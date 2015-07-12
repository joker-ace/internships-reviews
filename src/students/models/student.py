# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from common.models.university import University
from common.models.faculty import Faculty


class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    university = models.ForeignKey(University)
    faculty = models.ForeignKey(Faculty)
    is_studying = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode('Student: ' + self.user)

    def __str__(self):
        return unicode(self)
