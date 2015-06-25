# -*- coding: utf-8 -*-
from django.conf.urls import url
from students.views.registration_view import RegistrationView

urlpatterns = [
    url(r'registration/$', RegistrationView.as_view(), name='registration'),
]