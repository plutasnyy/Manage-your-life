from django.shortcuts import render
from django.http import HttpResponseRedirect
from note.models import Note as Note_model

def Homepage(request):
    if request.user.is_authenticated():
        username = request.user.username
        notes_list=Note_model.objects.all()
        return render(request,'note.html',{'notes_list':notes_list})
    else:
        return HttpResponseRedirect('/')
