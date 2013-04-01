from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
                       (r'^import', TemplateView.as_view(template_name='partials/import.html')),
                       (r'^start', TemplateView.as_view(template_name='partials/start.html')),
                       )