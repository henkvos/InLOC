# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from auth.views import LogOut
from home.views import Home
from utils.views import XMLImportView

admin.autodiscover()

urlpatterns = patterns('',

    (r'^api/', include('api.urls')),

    (r'^grappelli/', include('grappelli.urls')),
    (r'^partials/', include('partials.urls')),

    (r'^import/', XMLImportView.as_view()),

    (r'^logout/', LogOut.as_view()),
    (r'^admin/logout/', LogOut.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', Home.as_view()),
)