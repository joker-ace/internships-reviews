# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect


class CommonBaseView(View):
    form = None
    template_name = None
    context = {}

    def add_form_error(self, field, error_message=''):
        if self.form:
            self.form.add_error(field, error_message)


    def response(self, request):
        # TODO: complete common view
        pass