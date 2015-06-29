# -*- coding: utf-8 -*-
from django import forms
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    password = forms.CharField(required=True)

    def set_email_not_exists_error(self):
        self.add_error('email', 'Email not found in the system.')

    def set_invalid_password_error(self):
        self.add_error('password', 'Invalid password.')

    def get(self, field_name):
        return self.cleaned_data.get(field_name, '')