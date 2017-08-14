from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from todo_list.models import List as List_model
from todo_list.models import Item as Item_model

from todo_list.forms import ListForm, ItemForm

from django.views.decorators.csrf import ensure_csrf_cookie

def get_queryset():
    queryset=dict()
    for i in List_model.objects.all():
        queryset[i]=Item_model.objects.all().filter(list=i)
    return queryset

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

def json_response(form,data,request):
    queryset=get_queryset()
    data['queryset'] = render_to_string('todo_list_list.html', {
        'queryset': queryset,
    })

    context = {'form': form}
    data['html_form'] = render_to_string('todo_list_add_list.html',
        context,
        request=request
    )
    return JsonResponse(data)

def list_create(request):
    data = dict()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            new_list=form.save(commit=False)
            new_list.created_by=request.user
            new_list.save()
            data['form_is_valid'] = True

        else:
            data['form_is_valid'] = False
    else:
        form = ListForm()

    return json_response(form,data,request)

def item_create(request,pk):
    data = dict()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item=form.save(commit=False)

            queryset=List_model.objects.all().filter(id=pk)
            new_item.list=queryset[0]
            new_item.save()
            data['form_is_valid'] = True

        else:
            data['form_is_valid'] = False
    else:
        form = ItemForm()

    return json_response(form,data,request)

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('todo_list:Todo Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('todo_list:Todo Homepage')
