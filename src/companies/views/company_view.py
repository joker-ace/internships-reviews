# -*- coding: utf-8 -*-

from common.views.common_base_view import CommonBaseView


class CompanyView(CommonBaseView):
    template_name = 'companies/company.html'

    def get(self, request, company_id):
        company = self.data.companies.get_company_by_id(company_id)
        company_ratings = self.data.companies.get_company_average_rating(company_id)
        company = company.to_dict()
        company.update(company_ratings and company_ratings[0] or {})

        reviews = self.data.companies.get_company_internships_reviews(company_id)

        self.update_context({
            'company': company,
            'reviews': reviews
        })

        return self.response()
