# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.views.generic.base import View
from django.shortcuts import redirect, render


from django.contrib.auth import authenticate
from django.contrib.auth.views import login as login_view


class LogOut(View):
    def get(self, request):
        logout(request)

        return redirect('/')


class LogIn(View):
    def get(self, request):
        user = request.user

        if request.user.is_authenticated():
            return render(request, 'app.html', {"user":user})

        else:
            tpl = "login.html"
            return login_view(request, template_name=tpl)

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(username=username, password=password)
        except:
            user = None


        if user is not None:

            if user.is_active:
                login_view(request, user)

            return redirect('/')

        else:
            tpl = "login.html"
            return login_view(request, template_name=tpl)