# -*- coding: utf-8 -*-
from django import forms

from students.models.student import Student


class StudentUniversityForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['university', 'faculty', 'is_studying']
