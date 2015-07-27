# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from companies.forms.company_form import CompanyForm


class CompanyReviewView(CommonBaseView):
    template_name = 'companies/company_review.html'
    form_class = CompanyForm

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'provinces': self.data.common.get_provinces_list(),
            'company_form': self.form_class()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        company_form = self.form_class(request.POST)
        if not company_form.is_valid():
            self.update_context({
                'company_form': company_form,
                'provinces': self.data.common.get_provinces_list()
            })
            return self.response()

        company = company_form.get('company')
        province = company_form.get('province')
        city = company_form.get('city')

        province = self.data.common.get_province_by_id(province)
        city = self.data.common.get_city_by_name(city)
        if not city:
            city = self.data.common.add_city(company_form.get('city'), province, return_new_instance=True)

        company = self.data.companies.get_company_by_name(company)
        if not company:
            self.data.companies.add_company(company_form.get('company'), city)
        else:
            self.data.companies.add_company_office(company, city)

        self.update_context({
            'company_form': company_form,
            'provinces': self.data.common.get_provinces_list()
        })
        return self.response()
