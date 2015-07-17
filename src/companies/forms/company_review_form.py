# -*- coding: utf-8 -*-
from django import forms


class CompanyReviewForm(forms.Form):
    logo_image = forms.ImageField()
