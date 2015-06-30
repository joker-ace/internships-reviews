# -*- coding: utf-8 -*-
from django.conf.urls import url
from students.views.registration_view import RegistrationView
from students.views.login_view import LoginView
from students.views.logout_view import LogoutView

urlpatterns = [
    url(r'registration/$', RegistrationView.as_view(), name='registration_page'),
    url(r'login/$', LoginView.as_view(), name='login_page'),
    url(r'logout/$', LogoutView.as_view(), name='logout_page')
]
