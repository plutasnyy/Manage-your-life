from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from todo_list.models import List as List_model
from todo_list.models import Item as Item_model

from todo_list.forms import ListForm, ItemForm

def TodoList(request):
    if request.user.is_authenticated():
        queryset={}
        for i in List_model.objects.all():
            queryset[i]=Item_model.objects.all().filter(list=i)

        if request.method=='POST':
            form=ListForm(request.POST)
            if form.is_valid:
                new_list=form.save(commit=False)
                new_list.created_by=request.user
                new_list.save()
                return HttpResponseRedirect('/todo_list')
        else:
            form=ListForm()
            form2=ItemForm()
            return render(
                request,'todo_list.html',{
                    'queryset':queryset,
                    'ListForm':form,
                    'ItemForm:':form2,
                    }
                )
    else:
        return HttpResponseRedirect('/')

class TodoEdit(UpdateView):
    pass

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('todo_list:Todo Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('todo_list:Todo Homepage')
