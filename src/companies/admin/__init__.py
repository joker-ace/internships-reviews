# -*- coding: utf-8 -*-
from django.contrib import admin

from companies.models.company import Company
from companies.models.company_internship_review import CompanyInternshipReview

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


admin.site.register(CompanyInternshipReview)