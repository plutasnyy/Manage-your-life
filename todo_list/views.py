from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from todo_list.models import List as List_model
from todo_list.models import Item as Item_model

from todo_list.forms import ListForm, ItemForm

from django.views.decorators.csrf import ensure_csrf_cookie

def TodoList(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        queryset=get_queryset()

        return render(
            request,'todo_list.html',{
                'queryset':queryset,
                }
            )

def get_queryset():
    queryset=dict()
    for i in List_model.objects.all():
        queryset[i]=Item_model.objects.all().filter(list=i)
    return queryset

def save_object(request,model_form,path,user=None,item_list=None):
    data=dict()
    if request.method == 'POST':
        if model_form.is_valid():
            new_object=model_form.save(commit=False)

            if user is not None:
                new_object.created_by=user

            if item_list is not None:
                new_object.list=item_list

            new_object.save()
            data['form_is_valid'] = True

            queryset=get_queryset()
            data['queryset'] = render_to_string('todo_list_list.html', {
                'queryset': queryset,
            })

        else:
            data['form_is_valid'] = False

    context = {'form': model_form}
    data['html_form'] = render_to_string(path,
        context,
        request=request
    )
    return JsonResponse(data)

def list_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
    else:
        form = ListForm()
    return save_object(request,form,'todo_list_add_list.html',user=request.user)

def item_create(request,pk):
    item_list=None
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            queryset=List_model.objects.all().filter(id=pk)
            item_list=queryset[0]
    else:
        form = ItemForm()
    return save_object(request,form,'todo_list_add_item.html',item_list=item_list)

def list_edit(request,pk):
    List=get_object_or_404(List_model,id=pk)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=List)
    else:
        form = ListForm(instance=List)
    return save_object(request,form,'todo_list_edit_list.html')

def item_edit(request,pk):
    data=dict()
    Item=get_object_or_404(Item_model,id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=Item)
    else:
        form = ItemForm(instance=Item)
    return save_object(request,form,'todo_list_edit_item.html')

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('todo_list:Todo Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('todo_list:Todo Homepage')
