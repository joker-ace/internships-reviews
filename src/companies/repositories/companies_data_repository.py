# -*- coding: utf-8 -*-
from django.db.models import Avg

from companies.models.company import Company
from companies.models.company_internship_review import CompanyInternshipReview


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

    def get_company_internships_reviews(self, company):
        try:
            return CompanyInternshipReview.objects.get(company=company)
        except:
            pass

    def get_companies_average_ratings(self, companies_ids=None):
        if not companies_ids:
            return None

        return CompanyInternshipReview.objects.values('company').filter(
            company__id__in=set(companies_ids)
        ).annotate(
            recommendations_score=Avg('recommendation')
        ).annotate(
            apply_skills_score=Avg('apply_skills')
        ).annotate(
            learn_new_score=Avg('learn_new')
        )