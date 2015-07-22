# -*- coding: utf-8 -*-
from django import forms

from common.forms.base_form import BaseForm


class CompanyForm(BaseForm):
    company = forms.CharField(max_length=50, required=True)
    province = forms.IntegerField(required=True)
    city = forms.CharField(max_length=50, required=True)
