# -*- coding: utf-8 -*-
from django import forms

from common.forms.base_form import BaseForm
from companies.models.company_internship_review import CompanyInternshipReview


class CompanyReviewForm(forms.ModelForm, BaseForm):
    class Meta:
        model = CompanyInternshipReview
        exclude = ('user', 'company', 'pk', 'id', 'office', 'date')
