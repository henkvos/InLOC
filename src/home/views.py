# -*- coding: utf-8 -*-

from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login as login_view


class Home(View):

    def get(self, request):
        user = request.user

        if request.user.is_authenticated():

            return redirect('/admin/')

        #not authenticated, render login
        else:
            tpl = "_base.html"
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
            tpl = "_base.html"
            return login_view(request, template_name=tpl)
