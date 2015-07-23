# -*- coding: utf-8 -*-
from django import forms
from django.core import validators
from django.contrib.auth.models import User

from common.forms.base_form import BaseForm

class UserRegistrationForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User
        exclude = ('is_active', 'username', 'date_joined',)

    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    first_name = forms.CharField(
        required=True,
        validators=[validators.RegexValidator(r'^[a-zA-Z]{1,50}$')]
    )
    last_name = forms.CharField(
        required=True,
        validators=[validators.RegexValidator(r'^[a-zA-Z]{1,50}$')]
    )
    password = forms.CharField(required=True)
    password_confirmation = forms.CharField(required=True)

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if not password_confirmation:
            raise forms.ValidationError("You must confirm your password")

        if password != password_confirmation:
            raise forms.ValidationError("Your passwords do not match")
