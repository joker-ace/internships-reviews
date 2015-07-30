# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CompaniesListView(CommonBaseView):
    template_name = 'companies/list.html'
    companies_per_page = 5

    @method_decorator(login_required)
    def get(self, request):
        companies = Paginator(self.data.companies.get_companies_list(),
                              self.companies_per_page)
        page = request.GET.get('page')

        try:
            companies = companies.page(page)
        except PageNotAnInteger:
            companies = companies.page(1)
        except EmptyPage:
            companies = companies.page(companies.num_pages)

        self.update_context({
            'companies': companies
        })
        return self.response()
