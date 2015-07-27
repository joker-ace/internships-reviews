# -*- coding: utf-8 -*-
from django.contrib import admin

from companies.models.company import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    class CompanyOfficesInline(admin.TabularInline):
        model = Company.cities.through
        verbose_name_plural = 'offices'
        verbose_name = 'office'

    fieldsets = [
        ('Company information', {'fields': ['name', 'logo_image']})
    ]

    inlines = (CompanyOfficesInline,)
    exclude = ('cities',)
