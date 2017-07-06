from django.shortcuts import render
from django.contrib.auth import logout
from  django.http import HttpResponseRedirect

def Homepage(request):
    template_name='index.html'
    return render(request,'index.html',{})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
