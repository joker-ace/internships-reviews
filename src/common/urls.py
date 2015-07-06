# -*- coding: utf-8 -*-
from django.conf.urls import url

from common.views.university_faculties_view import UniversityFacultiesView

urlpatterns = [
    url(r'university/faculties/get', UniversityFacultiesView.as_view(), name='university_faculties_url'),
]
