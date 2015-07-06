# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.models.faculty import Faculty

from common.views.common_base_view import CommonBaseView


class UniversityFacultiesView(CommonBaseView):
    @method_decorator(login_required)
    def post(self, request):
        university = request.POST.get('university', '')
        try:
            university = int(university)
        except:
            return self.json_response({})

        faculties = Faculty.objects.filter(university=university)
        faculties = [dict(id=f.pk, name=f.name) for f in faculties]
        return self.json_response(faculties)
