# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse


class CommonBaseView(View):
    form_class = None
    template_name = None
    context = {}

    def update_context(self, context=None):
        if not context or not isinstance(context, dict):
            raise Exception('Invalid parameter for CommonBaseView.update_context method')
        self.context.update(context)

    def json_response(self, data=None):
        data = {'result': data}
        return JsonResponse(data)

    def response(self):
        return render(self.request, self.template_name, self.context)

    def redirect_to(self, view_name=None):
        if not view_name or not isinstance(view_name, (str, unicode)):
            raise Exception('Invalid parameter for CommonBaseView.redirect_to method')
        return redirect(to=view_name)
