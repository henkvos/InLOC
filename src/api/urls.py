from django.conf.urls import patterns, include, url

from l10n.views import LanguageList

urlpatterns = patterns('',
                       (r'^languages', LanguageList.as_view()),

                       )