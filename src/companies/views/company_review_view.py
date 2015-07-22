# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from companies.forms.company_form import CompanyForm
from companies.models.company import Company

class CompanyReviewView(CommonBaseView):
    template_name = 'companies/company_review.html'
    form_class = CompanyForm

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'form': self.form_class(),
            'companies': self.data.companies_data.get_companies_list(),
            'provinces': self.data.common.get_provinces_list()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        company_form = self.form_class(request.POST)
        if company_form.is_valid():
            company = company_form.get('company')
            province = company_form.get('province')
            city = company_form.get('city')
            if not self.data.companies_data.company_exists(company=company, province=province, city=city):
                company = self.data.companies_data.get_company_by_pk(company_form.get('company'))
                if not company:
                    company = Company()
                    company.name = company_form.get('company')

                company.id = None
                company.pk = None
                company.city = company_form.get('city')


        self.update_context({
            'company_form': company_form,
            'companies': self.data.companies_data.get_companies_list(),
            'provinces': self.data.common.get_provinces_list()
        })
        return self.response()
