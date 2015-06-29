# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from students.forms.login_form import LoginForm


class LoginView(View):
    template_name = 'students/login.html'
    form = LoginForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = None
            try:
                user = User.objects.get(username=form.get('email'))
            except User.DoesNotExist:
                form.set_email_not_exists_error()

            if user:
                if user.check_password(form.get('password')):
                    pass
                form.set_invalid_password_error()
            form.set_email_not_exists_error()
        context = {'form': form}
        return render(request, self.template_name, context)