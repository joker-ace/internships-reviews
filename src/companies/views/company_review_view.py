# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from companies.forms.company_review_form import CompanyReviewForm


class CompanyReviewView(CommonBaseView):
    template_name = 'companies/company_review.html'
    form_class = CompanyReviewForm

    def get(self, request):
        self.update_context({'form': self.form_class()})
        return self.response()
