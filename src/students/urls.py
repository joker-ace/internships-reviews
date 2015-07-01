# -*- coding: utf-8 -*-
from django.conf.urls import url
from students.views.registration_view import RegistrationView
from students.views.login_view import LoginView
from students.views.logout_view import LogoutView
from students.views.my_university_view import MyUniversityView

urlpatterns = [
    url(r'registration/$', RegistrationView.as_view(), name='registration_page'),
    url(r'login/$', LoginView.as_view(), name='login_page'),
    url(r'logout/$', LogoutView.as_view(), name='logout_page'),
    url(r'my/university/$', MyUniversityView.as_view(), name='my_university_page')
]
