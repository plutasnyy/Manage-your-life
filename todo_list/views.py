from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from todo_list.models import List as List_model
from todo_list.models import Item as Item_model


def TodoList(request):
    queryset={}
    for i in List_model.objects.all():
        queryset[i]=Item_model.objects.all().filter(list=i)


    return render(request,'todo_list.html',{'queryset':queryset})

class TodoEdit(UpdateView):
    pass

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('Todo_list Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('Todo_list Homepage')

class TodoCreate(CreateView):
    pass
