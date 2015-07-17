# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from common.models.faculty import Faculty
from students.models.student import Student


class StudentUniversityView(CommonBaseView):
    template_name = 'students/university.html'

    @method_decorator(login_required)
    def get(self, request):
        if self.data.users.university_record_exists(request.user):
            return self.redirect_to('companies_list_page')
        self.update_context({
            'universities': self.data.common.get_universities_list()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):

        if self.data.users.university_record_exists(request.user):
            return self.redirect_to('companies_list_page')

        university = self.data.common.get_university(request.POST.get('university'))
        faculty = request.POST.get('faculty')

        try:
            faculty = Faculty.objects.get(pk=faculty, university=university)
        except (Faculty.DoesNotExist, ValueError):
            faculty = Faculty.create(faculty, university)
            faculty.save()

        student = Student()
        student.university = university
        student.faculty = faculty
        student.is_studying = bool(request.POST.get('is_studying'))
        student.user = request.user
        student.save()
        return self.redirect_to('companies_list_page')
