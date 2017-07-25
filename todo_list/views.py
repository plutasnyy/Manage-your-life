from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from todo_list.models import List as List_model
from todo_list.models import Item as Item_model

from todo_list.forms import ListForm, ItemForm

def TodoList(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        queryset={}
        for i in List_model.objects.all():
            queryset[i]=Item_model.objects.all().filter(list=i)

        form=ListForm()
        return render(
            request,'todo_list.html',{
                'queryset':queryset,
                'form':form,
                }
            )

def list_create(request):
    form=ListForm()
    context={'form':form}
    html_form=render_to_string('todo_list_add_list.html',context,request=request)
    return JsonResponse({'html_form':html_form})

class TodoEdit(UpdateView):
    pass

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('todo_list:Todo Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('todo_list:Todo Homepage')
