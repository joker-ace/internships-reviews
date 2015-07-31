# -*- coding: utf-8 -*-

from common.views.common_base_view import CommonBaseView


class ApiAutocompleteCompanyName(CommonBaseView):
    def get(self, request):
        query = request.GET.get('q')
        companies = self.data.companies.find_companies_which_names_start_with(query)
        companies = [company.to_api_dict() for company in companies]
        return self.json_response(companies)
