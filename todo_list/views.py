from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from todo_list.models import List, Item

class TodoList(ListView):
    model = List
    queryset=List.objects.all()
    template_name='todo_list.html'

class TodoEdit(UpdateView):
    pass

class TodoDelete(DeleteView):
    pass

class TodoCreate(CreateView):
    pass
