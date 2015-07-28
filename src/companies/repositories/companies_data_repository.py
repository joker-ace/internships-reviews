# -*- coding: utf-8 -*-

from companies.models.company import Company


class CompaniesDataRepository(object):
    def get_companies_list(self):
        return Company.objects.order_by('name').all()

    def find_companies_which_names_start_with(self, query=None):
        companies = self.get_companies_list()
        if query:
            companies = companies.filter(name__istartswith=query)
        return companies

    def get_company_by_name(self, company_name):
        try:
            return Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            pass

    def add_company(self, company_name, city):
        company = Company()
        company.name = company_name
        company.save()
        company.cities.add(city)
        return company

    def add_company_office(self, company, city):
        company.cities.add(city)
        company.save()