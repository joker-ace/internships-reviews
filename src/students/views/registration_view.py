# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from students.forms.user_registration_form import UserRegistrationForm


class RegistrationView(View):
    template_name = 'students/registration.html'
    form = UserRegistrationForm

    def get(self, request):
        context = {'form': self.form()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            if User.objects.get(username=form.get('email')).exists():
                pass
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(user.password)
            user.save()

        context = {'form': form}
        return render(request, self.template_name, context)
