# -*- coding: utf-8 -*-
from django import forms
from django.core import validators

from common.forms.base_form import BaseForm


class LoginForm(BaseForm):
    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    password = forms.CharField(required=True)
