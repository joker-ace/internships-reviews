# -*- coding: utf-8 -*-

from companies.models.company import Company


class CompaniesDataRepository(object):
    def get_companies_list(self):
        return Company.objects.all()

    def company_exists(self, company, province, city):
        try:
            company = int(company)
            return Company.objects.filter(pk=company, province=province, city__iexact=city).exists()
        except ValueError:
            return Company.objects.filter(name=company, province=province, city__iexact=city).exists()

    def get_company_by_pk(self, company):
        try:
            return Company.objects.get(pk=company)
        except (Company.DoesNotExist, ValueError):
            return None
