from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import UpdateView

from note.models import Note as Note_model
from note.forms import NoteForm

def homepage(request):
    if request.user.is_authenticated():
        user = request.user
        notes_list=Note_model.objects.all().filter(created_by=user)
        notes_list=sorted(notes_list,key=lambda x:x.created_on,reverse=True)
        form = NoteForm(request.POST or None)
        
        if request.method == 'POST' and form.is_valid():
            new_note=form.save(commit=False)
            new_note.created_by=user
            new_note.save()
            return HttpResponseRedirect('/note')

        return render(request,'note.html',{'notes_list':notes_list,'form':form})

    else:
        return HttpResponseRedirect('/')

def note_delete(request,id):
    if request.method == 'POST':
        note=Note_model.objects.all().filter(id=id)
        note.delete()
    return HttpResponseRedirect('/note')

class NoteUpdate(UpdateView):
    model = Note_model
    fields = ['title','content']
    template_name='note_form.html'
    success_url='/note'
