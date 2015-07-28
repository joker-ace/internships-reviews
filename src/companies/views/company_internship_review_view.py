# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from common.views.common_base_view import CommonBaseView
from common.global_variables import REVIEW_ADDED_SUCCESSFULLY_MESSAGE

from companies.forms.company_form import CompanyForm
from companies.forms.company_review_form import CompanyReviewForm


class CompanyInternshipReviewView(CommonBaseView):
    template_name = 'companies/company_internship_review.html'

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'provinces': self.data.common.get_provinces_list(),
            'company_form': CompanyForm(),
            'review_form': CompanyReviewForm()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        company_form = CompanyForm(request.POST)
        review_form = CompanyReviewForm(request.POST)
        if not company_form.is_valid() or not review_form.is_valid():
            self.update_context({
                'company_form': company_form,
                'review_form': review_form,
                'provinces': self.data.common.get_provinces_list()
            })
            return self.response()
        company, city = self.process_company_data(company_form)
        self.add_company_review(company, city, review_form)
        messages.add_message(request, messages.SUCCESS, REVIEW_ADDED_SUCCESSFULLY_MESSAGE)
        return self.redirect_to(view_name='review_added_page')

    def add_company_review(self, company, city, review_form):
        review = review_form.save(commit=False)
        review.company = company
        review.office = city
        review.user = self.request.user
        review.save()

    def process_company_data(self, company_form):
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

        return company, city
