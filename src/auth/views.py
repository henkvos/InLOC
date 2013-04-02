# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.views.generic.base import View
from django.shortcuts import redirect


class LogOut(View):
    def get(self, request):
        logout(request)

        return redirect('/')