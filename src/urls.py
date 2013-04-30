# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from auth.views import LogOut, LogIn
from home.views import Home
from loc.views import LOCDefitionView, LOCStructureView, RdfView
from utils.views import XMLImportView

admin.autodiscover()

urlpatterns = patterns('',


    (r'^api/', include('api.urls')),
    (r'^view/locdefinition/(?P<id>[0-9]+)/$', LOCDefitionView.as_view()),
    (r'^view/locstructure/(?P<id>[0-9]+)/$', LOCStructureView.as_view()),
    (r'^view/rdf/(?P<id>[0-9]+)/$', RdfView.as_view()),

    (r'^grappelli/', include('grappelli.urls')),
    (r'^partials/', include('partials.urls')),

    (r'^import/', XMLImportView.as_view()),

    (r'^logout/', LogOut.as_view()),
    (r'^login/', LogIn.as_view()),
    (r'^admin/logout/', LogOut.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', Home.as_view()),
)