# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

FIRST_PAGE = 1

class CompaniesListView(CommonBaseView):
    template_name = 'companies/list.html'
    companies_per_page = 5

    def get(self, request):

        city = request.GET.get('city', '')
        faculty = request.GET.get('faculty', '')

        companies = Paginator(
            self.data.companies.get_companies_with_average_ratings_data(city, faculty),
            self.companies_per_page
        )
        page = request.GET.get('page')

        try:
            companies = companies.page(page)
        except PageNotAnInteger:
            companies = companies.page(FIRST_PAGE)
        except EmptyPage:
            companies = companies.page(companies.num_pages)

        self.update_context({
            'companies': companies
        })
        return self.response()
