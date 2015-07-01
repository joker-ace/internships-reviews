# -*- coding: utf-8 -*-
from common.views.common_base_view import CommonBaseView
from common.models.university import University


class MyUniversityView(CommonBaseView):
    template_name = 'students/university.html'

    def get(self, request):
        self.update_context({
            'universities': University.objects.all()
        })
        return self.response()