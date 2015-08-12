# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from students.views.home_view import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_page'),
    url(r'^students/', include('students.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)