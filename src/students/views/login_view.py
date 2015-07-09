# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from students.forms.login_form import LoginForm
from common.views.common_base_view import CommonBaseView
from common.global_variables import EMAIL_NOT_EXISTS_ERROR_MESSAGE, INVALID_PASSWORD_ERROR_MESSAGE, USER_IS_NOT_ACTIVE_MESSAGE


class LoginView(CommonBaseView):
    template_name = 'students/login.html'
    form = LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return self.redirect_to('companies_list_page')
        self.update_context({'form': self.form()})
        return self.response()

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            self.update_context({'form': form})
            return self.response()

        if not self.user_exists(form.get('email')):
            form.add_error('email', EMAIL_NOT_EXISTS_ERROR_MESSAGE)
            self.update_context({'form': form})
            return self.response()

        user = authenticate(username=form.get('email'), password=form.get('password'))
        if not user:
            form.add_error('password', INVALID_PASSWORD_ERROR_MESSAGE)
            self.update_context({'form': form})
            return self.response()

        if not user.is_active:
            form.add_error('email', USER_IS_NOT_ACTIVE_MESSAGE)
            self.update_context({'form': form})
            return self.response()

        login(request, user)

        return self.redirect_to('student_university_page')

    def user_exists(self, email):
        return User.objects.filter(username=email).exists()
