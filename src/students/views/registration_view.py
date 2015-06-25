# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render


class RegistrationView(View):
    template_name = 'students/registration.html'

    def get(self, request):
        return render(request, self.template_name)