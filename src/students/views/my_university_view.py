# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from common.views.common_base_view import CommonBaseView

from common.models.university import University
from students.models.student import Student
from students.forms.student_university_form import StudentUniversityForm


class MyUniversityView(CommonBaseView):
    template_name = 'students/university.html'

    @method_decorator(login_required)
    def get(self, request):
        self.update_context({
            'universities': University.objects.all()
        })

        if self.student_record_exists(request.user):
            return self.redirect_to('companies_list_page')

        return self.response()

    @method_decorator(login_required)
    def post(self, request):

        if self.student_record_exists(request.user):
            return self.redirect_to('companies_list_page')
        form = StudentUniversityForm(request.POST)
        if not form.is_valid():
            pass



        student = form.save(commit=False)
        student.user = request.user
        student.save()
        return self.redirect_to('companies_list_page')

    def student_record_exists(self, user):
        return Student.objects.filter(user=user).exists()
