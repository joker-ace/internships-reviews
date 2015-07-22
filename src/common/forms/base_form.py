# -*- coding: utf-8 -*-

from django import forms


class BaseForm(forms.Form):
    def get(self, field_name):
        return self.cleaned_data.get(field_name, '')
