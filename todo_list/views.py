from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from todo_list.models import List as List_model
from todo_list.models import Item as Item_model

from todo_list.forms import ListForm, ItemForm

def TodoList(request):
    queryset={}
    for i in List_model.objects.all():
        queryset[i]=Item_model.objects.all().filter(list=i)

    list_form=ListForm
    form=list_form(request.POST or None)
    if request.method=='POST':
        if form.is_valid:
            print("tu jestem:")
            new_list=form.save(commit=False)
            new_list.created_by=request.user
            print("tu tez")
            new_list.save()
            print("a tu nei")
            return HttpResponseRedirect('/todo_list')
    else:

        return render(
            request,'todo_list.html',{
                'queryset':queryset,
                'ListForm':form,
                }
            )

class TodoEdit(UpdateView):
    pass

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('Todo_list Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('Todo_list Homepage')
