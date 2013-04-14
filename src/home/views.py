# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.views import login as login_view


class Home(View):

    def get(self, request):
        user = request.user

        if request.user.is_authenticated():
            return render(request, 'app.html', {"user":user})

        else:
            tpl = "search.html"
            return login_view(request, template_name=tpl)
