from django import forms


class StudentUniversityForm(forms.Form):
    university = forms.IntegerField(required=True)
    faculty = forms.CharField(max_length=100, required=True)
    is_studying = forms.BooleanField()
