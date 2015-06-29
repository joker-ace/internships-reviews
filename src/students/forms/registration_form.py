# -*- coding: utf-8 -*-
from django import forms
from django.core import validators


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    first_name = forms.CharField(
        required=True,
        validators=[validators.RegexValidator(r'^[a-zA-Z]{1,50}$')]
    )
    last_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    repeat_password = forms.CharField(required=True)