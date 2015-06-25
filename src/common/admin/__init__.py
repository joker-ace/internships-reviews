# -*- coding: utf-8 -*-
from django.contrib import admin

from common.models.university import University
from common.models.faculty import Faculty
from common.models.company import Company

admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Company)