from django.shortcuts import render
from django.http import HttpResponseRedirect

from calendar_app.models import Event as EventModel
from calendar_app.forms import EventForm

def homepage(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request,'calendar.html',{'form':EventForm})

    else:
        return HttpResponseRedirect('/')
