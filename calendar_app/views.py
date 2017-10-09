from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from calendar_app.models import Event as EventModel
from calendar_app.forms import EventForm


from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

def homepage(request):
    if request.user.is_authenticated():
        form = EventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
        return render(request,'calendar.html',{'form':EventForm})
    else:
        return HttpResponseRedirect('/')
