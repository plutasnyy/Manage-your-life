from django.shortcuts import render
from django.contrib.auth import logout
from  django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

class Homepage(auth_views.LoginView):
    template_name='index.html'
