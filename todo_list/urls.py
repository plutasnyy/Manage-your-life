from django.conf.urls import url

import todo_list.views

urlpatterns=[
    url(r'todo_list^$',todo_list.views.TodoList,name='Homepage'),
    url(r'^delete/item/(?P<pk>[0-9]+)$',todo_list.views.TodoItemDelete.as_view(),name='Todo Item Delete'),
    url(r'^delete/list/(?P<pk>[0-9]+)$',todo_list.views.TodoListDelete.as_view(),name='Todo List Delete'),
    url(r'^edit/(?P<id>[0-9]+)$',todo_list.views.TodoEdit.as_view(),name='TodoEdit'),

]
