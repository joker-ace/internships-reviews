from django.conf.urls import url

from companies.views.companies_list_view import CompaniesListView

urlpatterns = [
    url(r'^$', CompaniesListView.as_view(), name='companies_list_page'),
]
