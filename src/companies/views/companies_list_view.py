# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CompaniesListView(CommonBaseView):
    template_name = 'companies/list.html'
    companies_per_page = 5

    def get(self, request):
        companies = Paginator(self.data.companies.get_companies_list(), self.companies_per_page)
        page = request.GET.get('page')

        try:
            companies = companies.page(page)
        except PageNotAnInteger:
            companies = companies.page(1)
        except EmptyPage:
            companies = companies.page(companies.num_pages)

        companies_list = {c.id: c.to_dict() for c in companies}
        companies_ratings = self.data.companies.get_companies_average_ratings(companies_ids=companies_list.keys())

        for rating in companies_ratings:
            id = rating['company']
            del rating['company']
            companies_list[id].update(rating)

        companies.object_list = companies_list.values()

        self.update_context({
            'companies': companies
        })
        return self.response()
