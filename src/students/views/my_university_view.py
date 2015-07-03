# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from common.models.university import University
from common.models.faculty import Faculty
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class MyUniversityView(CommonBaseView):
    template_name = 'students/university.html'

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'universities': University.objects.all(),
            'faculties': Faculty.objects.all()
        })
        return self.response()
