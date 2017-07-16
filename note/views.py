from django.shortcuts import render
from django.http import HttpResponseRedirect
from note.models import Note as Note_model
from note.forms import NoteForm

def Homepage(request):
    if request.user.is_authenticated():
        user = request.user
        notes_list=Note_model.objects.all().filter(created_by=user)

        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                new_note=form.save(commit=False)
                new_note.created_by=user
                new_note.save()
                return HttpResponseRedirect('/note')
        else:
            form = NoteForm()
        return render(request,'note.html',{'notes_list':notes_list,'form':form})
    else:
        return HttpResponseRedirect('/')

def note_delete(request,id):

    return HttpResponseRedirect('/')
