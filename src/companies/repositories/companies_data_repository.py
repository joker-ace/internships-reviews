# -*- coding: utf-8 -*-
from django.db.models import Avg
from django.db.models.functions import Coalesce

from companies.models.company import Company
from companies.models.company_internship_review import CompanyInternshipReview


class CompaniesDataRepository(object):

    def get_company_by_id(self, company_id):
        try:
            return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            pass

    def get_companies_list(self):
        return Company.objects.order_by('name').all()

    def get_companies_with_average_ratings_data(self, city=None, faculty=None):
        companies = Company.objects.values('name', 'id', 'logo_image').annotate(
            recommendations_score=Coalesce(Avg('companyinternshipreview__recommendation'), 0.0)
        ).annotate(
            apply_skills_score=Coalesce(Avg('companyinternshipreview__apply_skills'), 0.0)
        ).annotate(
            learn_new_score=Coalesce(Avg('companyinternshipreview__learn_new'), 0.0)
        ).order_by('-recommendations_score', '-apply_skills_score', '-learn_new_score')

        if city:
            companies = companies.filter(cities__name=city)

        if faculty:
            companies = companies.filter(companyinternshipreview__user__student__faculty__name=faculty)

        return companies

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
        return CompanyInternshipReview.objects.filter(company=company)

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

    def get_company_average_rating(self, company_id):
        if not company_id:
            return None

        return CompanyInternshipReview.objects.values('company').filter(
            company__id=company_id
        ).annotate(
            recommendations_score=Avg('recommendation')
        ).annotate(
            apply_skills_score=Avg('apply_skills')
        ).annotate(
            learn_new_score=Avg('learn_new')
        )