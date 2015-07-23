# -*- coding: utf-8 -*-
from django.contrib import admin

from common.models.university import University
from common.models.faculty import Faculty
from common.models.province import Province
from common.models.error_log import ErrorLog


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    class FacultyInline(admin.TabularInline):
        model = Faculty

    inlines = [FacultyInline]


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'message', 'error_url', 'stacktrace')


admin.site.register(Province)
admin.site.register(Faculty)
