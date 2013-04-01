from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from auth.views import LoginView, LogOut
from home.views import Home

urlpatterns = patterns('',

    (r'^grappelli/', include('grappelli.urls')),
    (r'^partials/', include('partials.urls')),
    (r'^admin/logout/', LogOut.as_view()),
    (r'^logout/', LogOut.as_view()),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', Home.as_view()),
)