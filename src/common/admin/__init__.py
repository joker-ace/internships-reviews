# -*- coding: utf-8 -*-
from django.contrib import admin

from common.models.university import University
from common.models.faculty import Faculty
from common.models.company import Company
from common.models.province import Province


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    class FacultyInline(admin.TabularInline):
        model = Faculty

    inlines = [FacultyInline]


admin.site.register(Province)
admin.site.register(Faculty)
admin.site.register(Company)