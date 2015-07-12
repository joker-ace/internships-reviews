# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from common.models.faculty import Faculty
from students.models.student import Student
from students.forms.student_university_form import StudentUniversityForm


class StudentUniversityView(CommonBaseView):
    template_name = 'students/profile.html'
    form_class = StudentUniversityForm

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'universities': self.data.common.get_universities_list()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        university = self.data.common.get_university(request.get('university'))
        faculty = request.POST.get('faculty')

        try:
            Faculty.objects.get(pk=faculty, university=university)
        except (Faculty.DoesNotExist, ValueError):
            faculty = Faculty.create(faculty, university)
            faculty.save()

        student = Student()
        student.university = university
        student.faculty = faculty
        student.is_studying = bool(request.POST.get('is_styding'))
        student.user = request.user
        student.save()
        return self.redirect_to('companies_list_page')
