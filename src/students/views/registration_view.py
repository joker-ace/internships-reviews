# -*- coding: utf-8 -*-
from django.contrib import messages

from common.views.common_base_view import CommonBaseView
from students.forms.user_registration_form import UserRegistrationForm
from common.global_variables import EMAIL_EXISTS_ERROR_MESSAGE, USER_REGISTERED_SUCCESSFULLY_MESSAGE


class RegistrationView(CommonBaseView):
    template_name = 'students/registration.html'
    form_class = UserRegistrationForm

    def get(self, request):
        if request.user.is_authenticated():
            return self.redirect_to('companies_list_page')
        self.update_context({'form': self.form_class()})
        return self.response()

    def post(self, request):
        if request.user.is_authenticated():
            return self.redirect_to('companies_list_page')
        form = self.form_class(request.POST)
        if not form.is_valid():
            self.update_context({'form': form})
            return self.response()

        if self.data.users.user_exists(form.get('email')):
            form.add_error('email', EMAIL_EXISTS_ERROR_MESSAGE)
            self.update_context({'form': form})
            return self.response()

        self.data.users.create_user(form)
        messages.success(request, USER_REGISTERED_SUCCESSFULLY_MESSAGE)
        return self.redirect_to('login_page')
