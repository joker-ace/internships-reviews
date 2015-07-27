# -*- coding: utf-8 -*-
from django.conf.urls import url

from companies.views.companies_list_view import CompaniesListView
from companies.views.company_review_view import CompanyReviewView


urlpatterns = [
    url(r'^list/$', CompaniesListView.as_view(), name='companies_list_page'),
    url(r'^add-company-review/$', CompanyReviewView.as_view(), name='company_review_page')
]
