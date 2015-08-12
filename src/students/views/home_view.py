# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView


class HomeView(CommonBaseView):

    template_name = 'students/home.html'

    def get(self, request):
        return self.response()
