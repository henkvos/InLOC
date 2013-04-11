from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
                       (r'^locstructure/add', TemplateView.as_view(template_name='partials/locstructure_add.html')),
                       (r'^locstructure', TemplateView.as_view(template_name='partials/locstructure.html')),
                       (r'^import', TemplateView.as_view(template_name='partials/import.html')),
                       (r'^start', TemplateView.as_view(template_name='partials/start.html')),

)