# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from common.views.common_base_view import CommonBaseView
from students.forms.user_registration_form import UserRegistrationForm
from common.global_variables import EMAIL_EXISTS_ERROR_MESSAGE, USER_REGISTERED_SUCCESSFULLY_MESSAGE


class RegistrationView(CommonBaseView):
    template_name = 'students/registration.html'
    form = UserRegistrationForm

    def get(self, request):
        if request.user.is_authenticated():
            return self.redirect_to('companies_list_page')
        context = {'form': self.form()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            self.update_context({'form': form})
            return self.response()

        if self.user_exists(form.get('email')):
            form.add_error('email', EMAIL_EXISTS_ERROR_MESSAGE)
            self.update_context({'form': form})
            return self.response()

        self.create_user(form)
        messages.success(request, USER_REGISTERED_SUCCESSFULLY_MESSAGE)
        return self.redirect_to('login_page')

    def create_user(self, model_form):
        user = model_form.save(commit=False)
        user.username = user.email
        user.set_password(user.password)
        user.save()

    def user_exists(self, email):
        return User.objects.filter(username=email).exists()
