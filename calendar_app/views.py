from django.shortcuts import render
from django.http import HttpResponseRedirect

def homepage(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request,'calendar.html',{})
    else:
        return HttpResponseRedirect('/')
