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

        return render(
            request,'todo_list.html',{
                'queryset':queryset,
                }
            )

def list_create(request):
    data = dict()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            Lists = List.objects.all()
            data['html_list_list'] = render_to_string('todo_list_list.html', {
                'queryset': Lists,
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ListForm()

    context = {'form': form}
    data['html_form'] = render_to_string('todo_list_add_list.html',
        context,
        request=request
    )
    return JsonResponse(data)


class TodoEdit(UpdateView):
    pass

class TodoItemDelete(DeleteView):
    model=Item_model
    success_url = reverse_lazy('todo_list:Todo Homepage')

class TodoListDelete(DeleteView):
    model=List_model
    success_url = reverse_lazy('todo_list:Todo Homepage')
