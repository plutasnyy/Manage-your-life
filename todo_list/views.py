from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from todo_list.models import List, Item

def TodoList(request):
    queryset={}
    for i in List.objects.all():
        queryset[i]=Item.objects.all().filter(list=i)

    print(queryset)

    return render(request,'todo_list.html',{'queryset':queryset})

class TodoEdit(UpdateView):
    pass

class TodoDelete(DeleteView):
    pass

class TodoCreate(CreateView):
    pass
