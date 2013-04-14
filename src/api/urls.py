from django.conf.urls import patterns, include, url

from api.views import api_root
from l10n.views import LanguageList
from loc.views import LOCStructureList, LOCStructureDetail, LOCSearch



urlpatterns = patterns('',
                       url(r'^$', api_root),
                       url(r'^search$', LOCSearch.as_view(), name='search'),
                       url(r'^languages/$', LanguageList.as_view(), name='language-list'),
                       url(r'^locstructures/(?P<pk>[0-9]+)$', LOCStructureDetail.as_view(), name='locstructure-detail'),
                       url(r'^locstructures/$', LOCStructureList.as_view(), name='locstructure-list'),

                       #(r'^languages', LanguageList.as_view()),
                       #(r'^locstructures', LOCStructureList.as_view()),

                       )