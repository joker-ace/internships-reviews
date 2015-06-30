# -*- coding: utf-8 -*-
from django import forms
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    password = forms.CharField(required=True)

    def get(self, field_name):
        return self.cleaned_data.get(field_name, '')
