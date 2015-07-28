# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CompaniesListView(CommonBaseView):
    template_name = 'companies/list.html'

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'companies': None
        })
        return self.response()
