from django.contrib.auth import logout, login
from django.views.generic.base import TemplateView, View
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = "_base.html"


class LogOut(View):
    def get(self, request):
        logout(request)

        return redirect('/')