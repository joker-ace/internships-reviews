# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView
from common.models.university import University
from common.models.faculty import Faculty
from students.models.student import Student
from students.forms.student_profile_form import StudentProfileForm

class StudentProfileView(CommonBaseView):
    template_name = 'students/profile.html'
    form_class = StudentProfileForm

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'universities': University.objects.all()
        })
        return self.response()

    @method_decorator(login_required)
    def post(self, request):
        university = University.objects.get(pk=request.POST.get('university'))
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
