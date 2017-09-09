from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from calendar_app.models import Event as EventModel
from calendar_app.forms import EventForm

def homepage(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request,'calendar.html',{'form':EventForm})

    else:
        return HttpResponseRedirect('/')

def create_event(request):
    data = dict()

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            new_event = form.save(commit=False)
            new_event.created_by = request.user
            new_event.save()
        else:
            data['form_is_valid'] = False
    else:
        form = EventForm()

    context = {'form' : form}
    data['html_form'] = render_to_string(
        'calendar_create_event.html',context,request=request
        )
    return JsonResponse(data)
