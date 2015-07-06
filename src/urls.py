# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^students/', include('students.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
