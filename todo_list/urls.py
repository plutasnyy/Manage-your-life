from django.conf.urls import url

import todo_list.views

urlpatterns=[
    url(r'^$',todo_list.views.TodoList,name='Todo Homepage'),
    url(r'^list/create/$',todo_list.views.list_create,name='Todo List Create'),
    url(r'^item/create/(?P<pk>[0-9]+)$',todo_list.views.item_create,name='Todo Item Create'),
    url(r'^delete/item/(?P<pk>[0-9]+)$',todo_list.views.TodoItemDelete.as_view(),name='Todo Item Delete'),
    url(r'^delete/list/(?P<pk>[0-9]+)$',todo_list.views.TodoListDelete.as_view(),name='Todo List Delete'),
    url(r'^list/edit/(?P<pk>[0-9]+)$',todo_list.views.list_edit,name='Todo List Edit'),
    url(r'^item/edit/(?P<pk>[0-9]+)$',todo_list.views.item_edit,name='Todo Item Edit'),
]
