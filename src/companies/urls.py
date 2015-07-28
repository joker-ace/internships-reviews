# -*- coding: utf-8 -*-
from django.conf.urls import url

from companies.views.companies_list_view import CompaniesListView
from companies.views.company_internship_review_view import CompanyInternshipReviewView
from companies.views.review_added_view import ReviewAddedView

urlpatterns = [
    url(r'^list/$', CompaniesListView.as_view(), name='companies_list_page'),
    url(r'^add-company-review/$', CompanyInternshipReviewView.as_view(), name='company_review_page'),
    url(r'^review-added/$', ReviewAddedView.as_view(), name='review_added_page')
]
