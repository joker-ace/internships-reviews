# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from common.models.university import University


class MyUniversityView(CommonBaseView):
    template_name = 'students/university.html'

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'universities': University.objects.all()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        pass
