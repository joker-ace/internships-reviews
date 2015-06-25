# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

from students.forms.registration_form import RegistrationForm


class RegistrationView(View):
    template_name = 'students/registration.html'
    form = RegistrationForm

    def get(self, request):
        context = {'form': self.form()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            print 'valid'
        context = {'form': form}
        return render(request, self.template_name, context)