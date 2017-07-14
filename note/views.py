from django.shortcuts import render
from django.http import HttpResponseRedirect
from note.models import Note as Note_model
from note.forms import NoteForm

def Homepage(request):
    print("lol")
    print(request)
    if request.user.is_authenticated():
        username = request.user.id
        notes_list=Note_model.objects.all().filter(author=username)

        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/note')
        else:
            form = NoteForm()
        return render(request,'note.html',{'notes_list':notes_list,'form':form})
    else:
        return HttpResponseRedirect('/')
